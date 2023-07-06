import streamsync as ss
import python_weather
import asyncio
from bs4 import BeautifulSoup
import requests


# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

# Shows in the log when the app starts
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
print("Hello world!")
def find_weather():
    city_name = 'Athens'
    city_name = city_name + " weather"
    city_name = city_name.replace(" ", "+")
    res = requests.get(
        f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/182536?apikey=aBGzYoeogKAGFYVBQBCETk1C3G7DBfHc&metric=true')
    
    print("Loading...")
    print(res.text[0])
    try:
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc').getText().strip()
        time = soup.select('#wob_dts').getText().strip()
        info = soup.select('#wob_dc').getText().strip()
        temperature = soup.select('#wob_tm').getText().strip()

        print("Location: " + location)
        print("Temperature: " + temperature + "&deg;C")
        print("Time: " + time)
        print("Weather Description: " + info)
        temp = temperature
        if temp <= 14: mess = "kinda cold at:" + str(temp)
        if temp > 14 and temp <= 20: mess = "nice at:" + str(temp)
        if temp > 20 and temp <= 25: mess = "kinda hot at:" + str(temp)
        if temp > 25 and temp <= 28: mess = "hot at:" + str(temp)
        if temp > 28 : mess = "blazing hot at:" + str(temp)
        # returns the current day's forecast temperature (int)
        return "+Currently its " + mess + "in the Land Of Dept"
    except:
        print('Something Failed')
    
async def getweather():
# declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast from a city
        print('in async')
        weather = await client.get('Athens')
        temp = weather.current.temperature
        if temp <= 14: mess = "kinda cold at:" + str(temp)
        if temp > 14 and temp <= 20: mess = "nice at:" + str(temp)
        if temp > 20 and temp <= 25: mess = "kinda hot at:" + str(temp)
        if temp > 25 and temp <= 28: mess = "hot at:" + str(temp)
        if temp > 28 : mess = "blazing hot at:" + str(temp)
        # returns the current day's forecast temperature (int)
        return "+Currently its " + mess + "in the Land Of Dept"


initial_state = ss.init_state({
    "my_app": {
        "title": "Yasuocidal Blog"
    },
    "_my_private_element": 1337,
    "message": find_weather(),
    "counter": 26,
})
