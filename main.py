"""Real-Time Weather Detection  Application"""
#Author: Paila Jeevan
#TODO: Flipkart Internship Task
from Data import Weather
from Storage import logging

def main():
    city = input("Enter City: ") # Get city name from user
    Weather.weather_info(city) # Call the function to get weather
    logging.store_weather_data(city)


if __name__ == "__main__":
    main()
