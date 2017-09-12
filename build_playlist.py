

import scrape
import spotify

def create_playlist(artist):
    """
    (artist) -> playlist_link
    Returns a string containing a link to a public playlist on Spotify which includes the songs in the artists latest (non-empty) setlist.
    
    Args:
        artist: A string containing the name of the required musician or band.
        
    Raises:
        TypeError: If the input is of type other than string.
        ValueError: If no artist provided
        ValueError: If no sets are found for the artist.
    """         
    
    track_names = scrape.find_songs(artist)
    songs = [[artist,track_names[idx]] for idx in range(len(track_names))]
    playlist_link = spotify.generate_playlist(songs)
    
    return playlist_link
     

artist = str(raw_input('Please enter the name of artist to create playlist: \n')) # Request artist name from user
scrape.validate_input(artist) # Make sure input is "legal"

print create_playlist(artist)
    

    
    