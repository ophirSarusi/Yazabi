
import spotipy
import spotipy.util as util

def Request_Authentication(username):
    """
    (username) -> sp
    Returns a Spotify API token with authentications to modify public and private playlists, and read the user library
        
    Args:
        username: A string containing the username to authenticate for.
            
    Raises:
        IOError: If the URL is unreachable.        
    """         
    
    client_id = "1efc2c5a25eb4d338fc0e562c57dbae1"
    client_secret = "f4706292e10c4069bd5c614983db2dde"
    redirect_uri = "http://localhost:8888/callback"
    scope = 'playlist-modify-private playlist-modify-public user-library-read'
    
    try:
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        sp = spotipy.Spotify(auth=token) 
    except:
        raise IOError('URL is unreachable or username invalid')
        
    return sp


def validate_and_cast_input(songs):
    """
    (songs) -> songs_str
    Checks the validity of given song list and casts all elements in list to type string.
        
    Args:
        songs: A list of strings to validate.
            
    Raises:
        ValueError: If the input list is empty
        TypeError: if the input list elements cannot be cast to string
    """     
    
    if len(songs) == 0:
        raise ValueError('Input cannot be empty!')
    
    songs_str = songs
    for idx in range(len(songs)):
        try: 
            songs_str[idx][0] = str(songs[idx][0])
            songs_str[idx][1] = str(songs[idx][1])
        except:
            raise TypeError('Input must be a string!')
        
    return songs_str


def generate_playlist(songs):
    """
    (songs) -> playlist_link
    Returns a link to a Spotify playlist containing the songs from the input list
        
    Args:
        songs: A list of lists of strings containing names of songs with their artist to include in playlist.
    
    Raises:
        ValueError: If a combination of artist and song cannot be found on Spotify            
    """         
    
    songs_str = validate_and_cast_input(songs) 
    #songs_str = songs
    
    username = "22dmso76lemvmxez6da4qw5wi"
    playlist_name = "Python Skill Test"    
    
    # Authorization into Spotify
    sp = Request_Authentication(username)

    
    # Scrape XML and obtain Spotify track ids based on track names 
    tracks=[]
    track_ids=[]
    for idx in range(len(songs_str)):
        search_result = sp.search(q='artist:{0} track:{1}'.format(songs_str[idx][0], songs_str[idx][1]), limit=1, offset=0, type='track', market=None)         
        tracks.append(search_result)
        try:        
            track_ids.append(tracks[idx]['tracks']['items'][0]['id'])
        except:
            raise ValueError("The combination of artist name: \"{0}\" and song name: \"{1}\" cannot be found on Spotify".format(songs_str[idx][0], songs_str[idx][1]))
    
    # Create playlist
    result1 = sp.user_playlist_create(username, playlist_name, public=True)
    playlist_id = result1['id']
    
    # Add tracks to the created playlist
    sp.user_playlist_add_tracks(username, playlist_id, tracks=track_ids)
    
    playlist_link = "https://open.spotify.com/user/" + username + "/playlist/" + playlist_id
        
    return playlist_link


