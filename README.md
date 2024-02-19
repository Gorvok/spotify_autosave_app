<h1>Spotify Fav Artist Auto-Save</h1>

Automatically discovers and saves new releases from your favorite artists directly to your Spotify library. This Flask-based application uses the Spotify Web API and OAuth 2.0 authentication to ensure you never miss out on new music from artists you love.

<h3>Features</h3>

1. OAuth 2.0 Authentication: Securely authenticate with Spotify using OAuth 2.0.
2. Artist Tracking: Specify the artist(s) you want to follow for new releases.
3. Automatic Saving: Automatically save new releases from your favorite artists to your Spotify library.
4. Filtering: Ensures that only tracks not already in your library are saved, avoiding duplicates.

<h3>Built With</h3>

1. Python - The programming language used.
2. Flask - The web framework used.
3. Spotify Web API - Used to fetch artist albums and manage saved tracks.

<h3>Getting Started</h3>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<h3>Prerequisites</h3>

1. Python 3.8 or higher
2. A Spotify Developer account and a registered Spotify application

<h3>Installation</h3>

1. Clone the Repository

```
git clone https://github.com/yourusername/project-name.git
cd project-name
```

2. Install required packages

```
pip install -r requirements.txt
```

3. Set Up environment variables

```
SPOTIFY_CLIENT_ID='your_spotify_client_id_here'
SPOTIFY_CLIENT_SECRET='your_spotify_client_secret_here'
```

Ensure .env is listed in your .gitignore file to keep your credentials secure.


4. Don't forget to change the Artist ID to your fav artist

ex. https://open.spotify.com/artist/7LVC96BEVGugTAp38AajV6 (Everything After the "artist/" so the 7LVC96BEVGugTAp38AajV6)

5. Run the application

```
python3 YOUR_FILE_NAME.py
```

Navigate to http://localhost:8888/login to authenticate with Spotify and start the process.

<h3>Usage</h3>

After authentication, the application will periodically check for new releases from the specified artist(s) and automatically save them to your Spotify library.

<h3>Contributing</h3>

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

<h3>License</h3>

This project is licensed under the MIT License - see the LICENSE file for details.

<h3>Acknowledgments</h3>

1. Spotify for providing a rich Web API.
2. Flask for an easy-to-use web framework.
3. All contributors who helped to improve the project.

<h3>Contact</h3>

Gjovani Gorvokaj

hello@gjo.dev

X: @gorvok_5

Instagram: @gorvok_5

https://www.gjo.dev
