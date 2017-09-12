
import requests

def get_temp_humid(coordinates,weather_url):
    """
    (coordinates, weather_url) -> temp , humid
    Returns the temperature and humidity at given coordinates, by requesting it from given URL.
        
    Args:
        coordinates: A Tuple containing the latitude and longitude of the desired location.
        weather_url: A string containing URL to request weather from (url includes required API)
            
    Raises:
        IOError: If the URL is unreachable.
        KeyError: If the API passed through the URL is invalid.
    """         
    
    try:
        r = requests.get(weather_url.format(coordinates[0],coordinates[1]))
        json_object = r.json()
    except:
        raise IOError('URL is unreachable at the moment. Please check your internet connection!')
        
    try:
        temp = float(json_object['main']['temp'])
        humid = float(json_object['main']['humidity'])
        return temp,humid
    except:
        raise  KeyError('Oops... your API key is invalid!')
   
def input_validation(coordinates):
    """
    (coordinates) -> no output
    Checks the validity of given coordinates.
        
    Args:
        coordinates: A Tuple containing the latitude and longitude of the desired location.
            
    Raises:
        TypeError: If the input is not of type tuple, or if elements inside tuple are not of type float.
        ValueError: If the tuple does not contain exactly 2 elements, or if elements exceed allowed range.
    """     
    
    if type(coordinates) != tuple:
        raise TypeError('Input must be a Tuple!')
    if len(coordinates) != 2:
        raise ValueError('Input Tuple must contain exactly two elements - Latitude and longitude!')
    if type(coordinates[0]) != float or type(coordinates[1]) != float: 
        raise TypeError('Input coordinates must be of type Float!')                  
    if coordinates[0]<-90 or coordinates[0]>90:
        raise ValueError('Latitude values must be between -90 and +90')        
    if coordinates[1]<-180 or coordinates[1]>180:
        raise ValueError('Longitude values must be between -180 and +180')  

def check_weather(coordinates):
    """
    (coordinates) -> no output
    Prints the temperature and humidity at given coordinates.
        
    Args:
        coordinates: A Tuple containing the latitude and longitude of the desired location.
            
    Raises:
        TypeError: If the input is not of type tuple, or if elements inside tuple are not of type float.
        ValueError: If the tuple does not contain exactly 2 elements, or if elements exceed allowed range.
    """     
    
    input_validation(coordinates)
    weather_url = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID=750f7caa81005f72c5d63d9e07af8d18&units=metric"
    temp,humid = get_temp_humid(coordinates,weather_url)
    
    print(u'Temperature is {0}\u00b0C, and humidity is {1}%'.format(temp,humid))
    
    
