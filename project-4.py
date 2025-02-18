import requests

def get_weather(api_key, location):
    # URL for the OpenWeatherMap API with the city as the parameter
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the full URL for the API call
    complete_url = base_url + "q=" + location + "&appid=" + api_key + "&units=metric"
    
    # Send a GET request to the API
    response = requests.get(complete_url)
    
    # Convert the response to JSON
    data = response.json()

    # Check if the city was found
    if data["cod"] == "404":
        print("Invalid city name or location. Please try again.")
        return

    # Extract the main data
    main_data = data["main"]
    weather_data = data["weather"][0]
    
    # Extract relevant information
    temperature = main_data["temp"]
    humidity = main_data["humidity"]
    weather_condition = weather_data["description"]
    
    # Print out the weather information
    print(f"Weather for {location.capitalize()}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_condition.capitalize()}")

def main():
    print("Welcome to the Weather App!")
    
    # Get the API key (replace with your actual API key)
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    
    # Get user input for the location (city or ZIP code)
    location = input("Enter the city or ZIP code: ").strip()
    
    # Fetch and display weather
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
