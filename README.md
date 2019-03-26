# PyOpenWeather
This is a module that allows for easier interfacing with the [Open Weather Map API](https://openweathermap.org/api) 

## pyopenweather.apikey
A string that must be set to the API key provided by the Open Weather Map website

## pyopenweather.getWeatherZip(zip, [format]):
```python
print(pyopenweather.getWeatherZip('90001', 'imperial').temp)
```
Returns a WeatherObject from the data presented
### *(str)* zip:
The zip code of the location you want to get data for
### *(str)* format (optional):
The format you want the data in (imperial, metric, or kelvin). The default is metric

## pyopenweather.getWeatherCoords(lat, lon, [format]):
```python
print(pyopenweather.getWeatherCoords('36.7783', '119.4179', 'kelvin').sunset)
```
Returns a WeatherObject from the data presented
### *(str)* lat:
The latitude of the location you want to get data for
### *(str)* lon:
The longitude of the location you want to get data for
### *(str)* format (optional):
The format you want the data in (imperial, metric, or kelvin). The default is metric

## pyopenweather.getWeatherID(id, [format]):
```python
print(pyopenweather.getWeatherID('2172797').humidity)
```
Returns a WeatherObject from the data presented
### *(str)* id:
The ID of the location you want to get data for. IDs can be found [here](http://bulk.openweathermap.org/sample/)
### *(str)* format (optional):
The format you want the data in (imperial, metric, or kelvin). The default is metric

## pyopenweather.WeatherObject:
Returns an object with the following
### *(str)* temp:
The current temperature at the location provided
### *(str)* mintemp:
The minimum temperature for the day at the location provided
### *(str)* maxtemp:
The maximum temperature for the day at the location provided
### *(str)* sunrise:
The time of sunrise at the location provided with the format
### *(str)* sunset:
The time of sunset at the location provided with the format
### *(str)* humidity:
The humidity percentage at the location provided
### *(str)* precipitation:
Whether or not it is raining in the city provided
### *(str)* cityname:
The name of the city provided
### *(str)* description:
A brief description of the current weather at the location provided
### *(str)* pressure:
The air pressure in hPa
### *(function)* getDict():
Returns a dict with all the same labels listed previously, if you want that sorta thing

## Example:
```python
import pyopenweather

pyopenweather.apikey = '(api key)'
weather = pyopenweather.getWeatherCoords('34.0522', '-118.2437', 'imperial')
print('The current weather is ' + weather.temp + ' in ' + weather.cityname)
```