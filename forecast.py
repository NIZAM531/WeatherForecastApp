import requests

# Map weather conditions to emojis
def get_weather_icon(condition):
    condition = condition.lower()
    if "sunny" in condition or "clear" in condition:
        return "☀️"
    elif "cloud" in condition:
        return "☁️"
    elif "rain" in condition or "drizzle" in condition:
        return "🌧️"
    elif "thunder" in condition or "storm" in condition:
        return "⛈️"
    elif "snow" in condition or "sleet" in condition:
        return "❄️"
    elif "fog" in condition or "mist" in condition or "haze" in condition:
        return "🌫️"
    else:
        return "🌍"  # default icon

def get_weather_forecast(city):
    # Replace with your WeatherAPI key
    api_key = "your_api_key"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}q={city}&days=7&aqi=no&alerts=no"

    response = requests.get(url)
    data = response.json()

    if "error" not in data:
        forecast = {
            "location": f"{data['location']['name']}, {data['location']['country']}",
            "current_temp": data['current']['temp_c'],
            "condition": data['current']['condition']['text'],
            "days": []
        }

        for day in data['forecast']['forecastday']:
            forecast['days'].append({
                "date": day['date'],
                "max_temp": day['day']['maxtemp_c'],
                "min_temp": day['day']['mintemp_c'],
                "condition": day['day']['condition']['text']
            })

        return forecast
    else:
        return None

def main():
    print("🌦 Simple 7-Day Weather Forecast 🌦")
    city = input("Enter city name: ")
    forecast = get_weather_forecast(city)

    if forecast:
        print(f"\n📍 Location: {forecast['location']}")
        print(f"🌡 Current Temp: {forecast['current_temp']}°C, {forecast['condition']}\n")

        print("🗓 7-Day Forecast:")
        print("-" * 70)
        print(f"{'Date':<12} | {'Condition':<20} | {'Min Temp (°C)':<14} | {'Max Temp (°C)':<14}")
        print("-" * 70)

        for day in forecast['days']:
            icon = get_weather_icon(day['condition'])
            print(f"{day['date']:<12} | {icon} {day['condition']:<18} | {day['min_temp']:<14} | {day['max_temp']:<14}")
        
        print("-" * 70)

    else:
        print("⚠️ Could not fetch weather. Please check the city name or API key.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")

