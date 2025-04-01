"""
Weather App Starter Code
------------------------
A simple Python application that fetches and displays current weather data
using the PyOWM (Python Open Weather Map) library.

Requirements:
- pip install pyowm
- Sign up for a free API key at: https://openweathermap.org/
"""


import pyowm
import datetime
import os
from pyowm.utils import config
from pyowm.utils import timestamps

# Configuration
API_KEY = "41fd1b300c46bf5cc9b44b107c5f4b45"  # Students will need to replace this with their own API key
DEFAULT_CITY = "New York"

class WeatherApp:
    def __init__(self, api_key):
        """Initialize the weather app with the API key."""
        self.owm = pyowm.OWM(api_key)
        self.mgr = self.owm.weather_manager()
        print("Weather App initialized!")
        
    def get_current_weather(self, city):
        """Get current weather data for the specified city."""
        try:
            observation = self.mgr.weather_at_place(city)
            weather = observation.weather
            return weather
        except Exception as e:
            print(f"Error getting weather for {city}: {e}")
            return None
            
    def display_weather(self, city):
        """Display current weather information for the specified city."""
        weather = self.get_current_weather(city)
        if weather:
            # Get data
            status = weather.detailed_status
            temperature = weather.temperature('celsius')
            humidity = weather.humidity
            wind = weather.wind()
            sunrise = weather.sunrise_time(timeformat='date')
            sunset = weather.sunset_time(timeformat='date')
            
            # Display information
            print("\n" + "="*50)
            print(f"Current Weather for: {city}")
            print("="*50)
            print(f"Status: {status.capitalize()}")
            print(f"Temperature: {temperature['temp']:.1f}°C")
            print(f"Feels like: {temperature['feels_like']:.1f}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind speed: {wind['speed']} m/s")
            print(f"Sunrise: {sunrise.strftime('%H:%M')}")
            print(f"Sunset: {sunset.strftime('%H:%M')}")
            print("="*50 + "\n")
        else:
            print(f"Unable to get weather information for {city}.")

def main():
    """Main function to run the Weather App."""
    print("Welcome to the Weather App!")
    print("---------------------------")
    
    # Initialize app
    app = WeatherApp(API_KEY)
    
    while True:
        # Get city input from user
        city = input(f"Enter a city name (or press Enter for default '{DEFAULT_CITY}'): ")
        if not city:
            city = DEFAULT_CITY
            
        # Display weather
        app.display_weather(city)
        
        # Ask user if they want to check another city
        choice = input("Would you like to check another city? (y/n): ").lower()
        if choice != 'y':
            print("Thank you for using the Weather App!")
            break

if __name__ == "__main__":
    main()
