import requests

def get_weather(city):
    api_key = "9d1543939a56a617c3c918a163fe2a44"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["cod"] == 200:
            display_weather(data)
        else:
            print("Error: City not found!")
    except requests.exceptions.HTTPError:
        print("Error: City not found!")
    except requests.exceptions.ConnectionError:
        print("Connection Error: Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Timeout Error: Request took too long.")
    except requests.exceptions.RequestException as req_error:
        print(f"Request Error: {req_error}")

def display_weather(data):
    temperature_k = data["main"]["temp"]
    temperature_c = temperature_k - 273.15
    weather_description = data["weather"][0]["description"]
    weather_emoji = get_weather_emoji(data["weather"][0]["id"])
    
    print(f"Temperature: {temperature_c:.0f}°C {weather_emoji}")
    print(f"Condition: {weather_description.capitalize()}")

def get_weather_emoji(weather_id):
    if 200 <= weather_id <= 232:
        return "⛈️"
    elif 300 <= weather_id <= 321:
        return "🌦️"
    elif 500 <= weather_id <= 531:
        return "🌧️"
    elif 600 <= weather_id <= 622:
        return "❄️"
    elif 701 <= weather_id <= 741:
        return "🎐"
    elif weather_id == 762:
        return "🌋"
    elif weather_id == 771:
        return "💨"
    elif weather_id == 781:
        return "🌪️"
    elif weather_id == 800:
        return "☀️"
    elif 801 <= weather_id <= 804:
        return "☁️"
    else:
        return ""

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
