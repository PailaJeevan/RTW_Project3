"""Real-Time Weather Detection  Application"""
#Author: Paila Jeevan
#TODO: Flipkart Internship Task
import requests 
import os
import csv 
from datetime import datetime # important import
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

class logging:
    # Storing Weather data in CSV file
  def store_weather_data(city):
    my_api_key = "8e564049b19165c70e94bb1f40c5f58c"
    url = "https://api.openweathermap.org/data/2.5/weather"
    values = {
        "q": city,  # City name
        "appid": my_api_key,  # API key
        "units": "metric" # Metric units for temperature in Celsius
    }
    try:
        resp = requests.get(url, params=values) 
        if resp.status_code == 200:
            data = resp.json() #Coverting the text resposnse into JSON format
            city_name = data["name"] # Store city name into city_name variable
            country = data["sys"]["country"] # store country code into country variable
            temperature = data["main"]["temp"] # store temperature into temperature variable
            feels_like = data["main"]["feels_like"] # store feels like temperature into feels_like variable
            humidity = data["main"]["humidity"] # store humidity into humidity variable
            condition = data["weather"][0]["description"].capitalize() # store weather condition into condition variable
            wind_speed = data["wind"]["speed"] # store wind speed into wind_speed variable


            filename = "weather_data.csv" # CSV file name to store weather data
            file_exists = os.path.isfile(filename) # Checking the file is already exists or not
            with open(filename, mode="a", newline="") as file: # Open the file for appending data
                writer = csv.writer(file) # Creating a csv writer object to write the data
                if not file_exists: # If the file is not already exists, write the header
                    writer.writerow(["Timestamp", "City", "Country", "Temperature (°C)", "Feels Like (°C)", "Humidity (%)", "Condition", "Wind Speed (m/s)"]) # Writing the header row in this format in csv file
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([timestamp, city_name, country, temperature, feels_like, humidity, condition, wind_speed]) # Writing the weather data get for api file into csv file
            print(f"\n Weather data for {city_name} stored in {filename}")
    except Exception as e: # Catching the expected errors 
        print("\n Error:", str(e))
        
def main():
    city = input("Enter City: ") # Get city name from user
    Weather.weather_info(city) # Call the function to get weather
    logging.store_weather_data(city)


if __name__ == "__main__":

    main()

