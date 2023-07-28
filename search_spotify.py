https://github.com/zbuchan/flask-musiccruncher.gitfrom spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import json
from flask import Flask, request
from flask_cors import CORS
import requests
import base64
from secrets import *


app = Flask(__name__)
CORS(app)

    
@app.route('/')
def hello():
    return json.dumps("hello world")

@app.route('/search',methods = ['POST'])
def foo():
    data = request.get_json()
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    result = sp.search(data["title"], market="us")
    print(json.dumps(result))
    d = {'alpha':json.dumps(result) , 'beta': 2}
    return json.dumps(d['alpha'])

    
    #sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    #result = sp.search(data["q"], market="us")

    #return json.dumps(result)

@app.route('/searchalbum',methods = ['POST'])
def fooo():
    data = request.get_json()
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    result = sp.search(data["title"], limit=20, type="album", market="us")

    

    list = []

    for item in result['albums']['items']:
        name = item['name']
        link = item['images'][0]['url']
        release = item['release_date']
        album = {
            'name' : name,
            'link' : link,
            'release' : release
        }    
        list.append(album)

    

    return json.dumps(list)

    
@app.route('/home',methods = ['GET'])
def ho():
    # data = request.get_json()
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    top_playlist = sp.featured_playlists(limit=10)

    tp = []
    for playlist in top_playlist['playlists']['items']:
        name = playlist['name']
        link = playlist['images'][0]['url']
        top_play = {
            'name' : name,
            'link' : link
        }
        tp.append(top_play)

    print(top_playlist)

    

    
    return tp
    #return json.dumps(tp)










# main driver function
if __name__ == '__main__':
 
    
    app.run(debug=True)
