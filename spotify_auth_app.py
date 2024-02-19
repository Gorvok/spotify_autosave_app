from flask import Flask, request, redirect, session
from dotenv import load_dotenv
from flask_session import Session
import requests
import os
import uuid
import json
load_dotenv()

app = Flask(__name__)

# Configure server-side session management
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
Session(app)

# Spotify OAuth 2.0 setup
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')  # Replace with your own client ID from Spotify for Developers.
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')  # Replace with your own client secret from Spotify for Developers.
REDIRECT_URI = 'http://localhost:8888/callback'

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
ARTIST_ID = '7LVC96BEVGugTAp38AajV6'  # Example artist ID Input replace with whichever artist is your favorite

@app.route('/login')
def login():
    state = str(uuid.uuid4())
    session['state'] = state
    scope = 'user-library-modify user-library-read'
    auth_url = f"{SPOTIFY_AUTH_URL}?response_type=code&client_id={CLIENT_ID}&scope={scope}&redirect_uri={REDIRECT_URI}&state={state}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    session_state = session.get('state', None)
    request_state = request.args.get('state', None)

    if session_state is None or request_state is None or session_state != request_state:
        return "State mismatch or missing. Please try logging in again.", 401

    code = request.args.get('code')
    auth_response = requests.post(SPOTIFY_TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    auth_response_data = auth_response.json()
    session['token'] = auth_response_data.get('access_token')

    if 'token' in session:
        return redirect('/fetch_and_save_new_tracks')
    else:
        return "Failed to retrieve access token.", 400

@app.route('/fetch_and_save_new_tracks')
def fetch_and_save_new_tracks():
    access_token = session.get('token')
    if not access_token:
        return "Access token is missing. Please login again.", 400

    headers = {"Authorization": f"Bearer {access_token}"}
    albums = fetch_artist_albums(ARTIST_ID, headers)
    new_tracks = filter_and_save_new_tracks(albums, headers)

    return f"Saved {len(new_tracks)} new tracks to your library."

def fetch_artist_albums(artist_id, headers):
    albums = []
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?include_groups=album,single&limit=50"
    while url:
        response = requests.get(url, headers=headers)
        data = response.json()
        albums.extend(data['items'])
        url = data.get('next')
    return albums

def filter_and_save_new_tracks(albums, headers):
    new_tracks = []
    for album in albums:
        album_id = album['id']
        tracks_response = requests.get(f"https://api.spotify.com/v1/albums/{album_id}/tracks", headers=headers)
        tracks_data = tracks_response.json()['items']
        for track in tracks_data:
            track_id = track['id']
            check_saved = requests.get(f"https://api.spotify.com/v1/me/tracks/contains?ids={track_id}", headers=headers)
            is_saved = check_saved.json()[0]
            if not is_saved:
                new_tracks.append(track_id)

    if new_tracks:
        for i in range(0, len(new_tracks), 50):
            chunk = new_tracks[i:i+50]
            requests.put("https://api.spotify.com/v1/me/tracks", headers=headers, json={"ids": chunk})
    return new_tracks

if __name__ == '__main__':
    app.run(port=8888, debug=True)
