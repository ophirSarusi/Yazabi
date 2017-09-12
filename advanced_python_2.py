
import advanced_python_1 as AP1
import unittest
import random

class TestMyFunctions(unittest.TestCase):
    """Test for advanced_python_1.py"""
    
    def test_input_not_tuple(self):
        """Is a TypeError successfully raised when input is not Tuple?"""        
        self.assertRaises(TypeError,AP1.input_validation,2)
        
    def test_input_not_2_elements(self):
        """Is a ValueError successfully raised when input Tuple is not 2 elements?"""
        self.assertRaises(ValueError,AP1.input_validation,(3,2,5))
    
    def test_input_not_float(self):
        """Is a TypeError successfully raised when input Tuple doesn't containt only floats?"""
        self.assertRaises(TypeError,AP1.input_validation,('t',2))
        
    def test_input_lat_illegal(self):
        """Is a ValueError successfully raised when input latitude is outside of allowed range?"""
        self.assertRaises(ValueError,AP1.input_validation,(100.01,100.01))
        
    def test_input_lon_illegal(self):
        """Is a ValueError successfully raised when input longitude is outside of allowed range?"""
        self.assertRaises(ValueError,AP1.input_validation,(30.22,190.01))
        
    def test_bad_URL(self):
        """Is a IOError successfully raised when the weather url is incorrect/unreachable?"""        
        self.bad_weather_url = "http://nothinghereeee.com/omgverytextmuchurl"
        self.assertRaises(IOError,AP1.get_temp_humid,(30.0444,31.2357),self.bad_weather_url)

    def test_bad_API(self):
        """Is a KeyError successfully raised when the weather API is invalid?"""
        self.bad_weather_api = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID=50f7caa81005f72c5d63d9e07af8d18&units=metric"
        self.assertRaises(KeyError,AP1.get_temp_humid,(30.0444,31.2357),self.bad_weather_api)

    def test_cairo_vs_SP(self):
        """Is the temperature in Cairo higher then the temperature at the South Pole?"""
        self.good_weather_url = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID=750f7caa81005f72c5d63d9e07af8d18&units=metric"
        self.cairo_t,self.cairo_h = AP1.get_temp_humid((30.0444,31.2357),self.good_weather_url)
        self.SP_t,self.SP_h = AP1.get_temp_humid((-90.00,0.00),self.good_weather_url)        
        self.assertGreater(self.cairo_t,self.SP_t)
        
    def test_random_humidity_legal(self):
        """Is the humidity in a random coordinate within the legal range?"""
        self.good_weather_url = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID=750f7caa81005f72c5d63d9e07af8d18&units=metric"
        self.lat = random.uniform(-90,90)
        self.long = random.uniform(-180,180)
        self.random_t,self.random_h = AP1.get_temp_humid((self.lat,self.long),self.good_weather_url)
        self.assertTrue( 0 <= self.random_h <= 100 )
        
if __name__ == '__main__':
    unittest.main()
    
    