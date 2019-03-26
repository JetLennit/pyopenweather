import xml.etree.ElementTree as ET
from urllib.request import urlopen
import urllib

apikey = ''

class WeatherObject:
    temp = ''
    mintemp = ''
    maxtemp = ''
    sunrise = ''
    sunset = ''
    humidity = ''
    precipitation = ''
    cityname = ''
    description = ''
    pressure = ''

    def getDict(self):
        weatherDict = {}
        weatherDict['temp'] = self.temp
        weatherDict['mintemp'] = self.mintemp
        weatherDict['maxtemp'] = self.maxtemp
        weatherDict['sunrise'] = self.sunrise
        weatherDict['sunset'] = self.sunset
        weatherDict['humidity'] = self.humidity
        weatherDict['precipitation'] = self.precipitation
        weatherDict['cityname'] = self.cityname
        weatherDict['description'] = self.description
        weatherDict['pressure'] = self.pressure
        return weatherDict

def __weatherObject(weather):
    currWeather = WeatherObject()
    if(weather is None):
        return currWeather

    weather = ET.fromstring(weather.decode('utf-8'))

    currWeather.temp = weather.find('temperature').get('value')
    currWeather.mintemp = weather.find('temperature').get('min')
    currWeather.maxtemp = weather.find('temperature').get('max')
    currWeather.sunrise = weather.find('city').find('sun').get('rise')
    currWeather.sunset = weather.find('city').find('sun').get('set')
    currWeather.humidity = weather.find('humidity').get('value')
    currWeather.precipitation = weather.find('precipitation').get('mode')
    currWeather.cityname = weather.find('city').get('name')
    currWeather.description = weather.find('weather').get('value')
    currWeather.pressure = weather.find('pressure').get('value')

    return currWeather

def __getURLXML(url):
    try:
        file = urlopen(url)
        xml = file.read()
        file.close()
        return xml
    except urllib.error.HTTPError:
        print('ERROR: Either the website is down or you have a bad API key')

def getWeatherZip(zipcode, units='metric'):
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + ',us&units=' + units + '&mode=xml&APPID=' + apikey
    print(url)
    xml = __getURLXML(url)
    return __weatherObject(xml)

def getWeatherID(id, units='metric'):
    url = 'http://api.openweathermap.org/data/2.5/weather?id=' + id + '&units=' + units + '&mode=xml&APPID=' + apikey
    print(url)
    xml = __getURLXML(url)
    return __weatherObject(xml)

def getWeatherCoords(lat, lon, units='metric'):
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&units=' + units + '&mode=xml&APPID=' + apikey
    print(url)
    xml = __getURLXML(url)
    return __weatherObject(xml)