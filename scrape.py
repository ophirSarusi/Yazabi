

import requests
from bs4 import BeautifulSoup


def find_songs(artist):
    """
    (url, artist) -> songs 
    Returns the names of the songs in the input artist latest (non-empty) setlist,
    by requesting an XML file from given URL and parsing the text.
        
    Args:
        artist: A string containing the name of the required musician or band.
            
    Raises:
        IOError: If the URL is unreachable.
        ValueError: If the artist was not found in the database
    """         

    url = "http://api.setlist.fm/rest/0.1/search/setlists.xml"
    
    try:
        r = requests.get(url , params={'artistName' : artist}) # request xml from url
        r_soup = BeautifulSoup(r.text, 'html.parser') # make soup with xml        
    except:
        raise IOError('URL is unreachable at the moment. Please check your internet connection!')
        
    try:    
        setlist = r_soup.song.find_parent("set").find_all("song") 
    except:
        raise ValueError('Sorry, no sets were found in the database for this artist...')
        
    songs = [BeautifulSoup(str(setlist[i]), 'html.parser').song['name'].encode('utf-8') for i in range(len(setlist))] # create list of song names using list of song tags
    
    return songs
    
    
def validate_input(artist):
    """
    (artist) -> no output
    Checks the validity of given artist name.
        
    Args:
        artist: A string containing the name of the required musician or band to validate.
            
    Raises:
        TypeError: If the input is empty or if the imput is not a string.
    """     
    
    if not artist:
        raise ValueError('Input cannot be empty!')
    if type(artist) != str:
        raise TypeError('Input must be a string!')
        
    pass

    
def get_songs():
    """
    (no input) -> songs
    Requests the user for an artist name, and obtains the names of the songs in the artist latest (non-empty) setlist.
            
    Raises:
        TypeError: If the input is of type other than string.
        ValueError: If no sets are found for the artist.
    """     
    
    artist = str(raw_input('Please enter the name of a musician or band to search: \n')) # Request artist name from user
    validate_input(artist) # Make sure input is "legal"
    
    songs = find_songs(artist)
    
    return songs
    

