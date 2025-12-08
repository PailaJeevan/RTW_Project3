import requests # request library to make HTTP requests
class Weather:
   
   def weather_info(city):
    my_api_key = "8e564049b19165c70e94bb1f40c5f58c"   # My OpenWeather API key
    url = "https://api.openweathermap.org/data/2.5/weather" #requesting this URL

    values = {
        "q": city, #city name
        "appid": my_api_key, #API key
        "units": "metric" #metric units for temperature in Celsius
    }

    try:
        resp = requests.get(url, params=values) 
        """resp stores the information from the API"""
        if resp.status_code == 404:
            print("\n City not found")
            return
        elif resp.status_code == 401:
            print("\n Invalid API key")
            return
        elif resp.status_code == 429:
            print("\n API rate limit exceeded")
            return
        elif resp.status_code == 500:
            print("\n Server error at OpenWeatherMap")
            return
        elif resp.status_code == 200:
            data = resp.json() #Coverting the text resposnse into JSON format
            print(f"\nWeather in {city.title()}:") #show the city name
            print(f" Temperature: {data['main']['temp']}°C") #show temperature
            print(f" Feels Like: {data['main']['feels_like']}°C") #show feels like temperature
            print(f" Condition: {data['weather'][0]['description'].capitalize()}") #show weather condition
            print(f" Humidity: {data['main']['humidity']}%") #show humidity
            print(f" Wind Speed: {data['wind']['speed']} m/s") #show wind speed
        else:
            print("\n City not found or API error") #if city nof found show this message
    except Exception as e:
        print("\n Error:", str(e))
