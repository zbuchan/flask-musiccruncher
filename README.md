# flask-musiccruncher
This is a Flask application that provides a REST api to Spotify. It is to be used in conjunction with this Vue.js application, [https://github.com/zbuchan/vue-musiccruncher].

# Project Set-Up
Need to have a Spotify app, here are direct instructions how to create that are here, [https://developer.spotify.com/documentation/web-api].
Once you have created the Spotify app, you need to set up the two enviorment variables, which are the client id and the client secret.
```
export SPOTIPY_CLIENT_ID=
export  SPOTIPY_CLIENT_SECRET=
```
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python search_spotify.py
```
