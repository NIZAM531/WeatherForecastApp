# 7-Day Weather Forecast App

A beginner-friendly Python application that fetches **current weather** and a **7-day forecast** for any city using [WeatherAPI](https://www.weatherapi.com/). The app displays weather conditions with **emojis** and presents the forecast in a **clean table format**.
---
![image alt](https://github.com/NIZAM531/WeatherForecastApp/blob/4b8e58552014b6219b19de50cbe2fbacfa0ae25b/download%20(1).png)
## Features
- Fetches **current temperature** and weather condition for any city.
- Shows **7-day forecast** with min/max temperatures.
- **Emoji-based visualization** for weather conditions:
  - ☀️ Sunny / Clear
  - ☁️ Cloudy
  - 🌧️ Rain / Drizzle
  - ⛈️ Thunderstorm
  - ❄️ Snow / Sleet
  - 🌫️ Fog / Mist / Haze
- Tabular output for easy reading.
- Waits for user input before closing, so you can read the results.
---

## Installation

1. Make sure you have **Python 3.13** installed.
2. Install the `requests` library:

```bash
pip install requests## Usage

1. Open Command Prompt (Windows) or Terminal (macOS/Linux).
2. Navigate to the folder containing `forecast.py`:

```bash
cd path/to/your/folder

Run the script:
python forecast.py

API Key

You need a WeatherAPI key:
Sign up at WeatherAPI
```bash
api_key = "YOUR_API_KEY_" and {api-key}

Replace the api_key variable in forecast.py with your API key
 Enter your city name when prompted:
example,
```bash
Enter city name: Delhi

View the 7-day forecast table with emojis in the console.
