# -*- coding: utf-8 -*-
"""
Created on Fri May 05 15:07:04 2017

@author: Ophir
"""


import spotipy
import spotipy.util as util

def generate_playlist(songs):
    
    client_id = "1efc2c5a25eb4d338fc0e562c57dbae1"
    client_secret = "f4706292e10c4069bd5c614983db2dde"
    redirect_uri = "http://localhost:8888/callback"
    username = "22dmso76lemvmxez6da4qw5wi"
    scope = 'playlist-modify-private playlist-modify-public';
           
    playlist_name = "temp"    
    
    token = util.prompt_for_user_token(username, scope)
    
    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        raise("Can't get token")

    result1 = sp.user_playlist_create(client_id, playlist_name, public=False)
    print(result1)
    print("****************")
    
    result2 = sp.user_playlist_add_tracks(client_id, playlist_id=playlist_name, tracks=songs)
    

    print(result2)
    
    pass