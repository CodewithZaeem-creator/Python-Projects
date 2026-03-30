"""Tkinter GUI weather application using Open-Meteo."""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Optional, Tuple

import requests
from geopy.exc import GeocoderServiceError
from geopy.geocoders import Nominatim

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODE_DETAILS = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫️"),
    48: ("Depositing rime fog", "🌫️"),
    51: ("Light drizzle", "🌦️"),
    53: ("Moderate drizzle", "🌦️"),
    55: ("Dense drizzle", "🌦️"),
    61: ("Light rain", "🌧️"),
    63: ("Moderate rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    66: ("Freezing rain", "🌧️"),
    67: ("Heavy freezing rain", "🌧️"),
    71: ("Light snow", "❄️"),
    73: ("Moderate snow", "❄️"),
    75: ("Heavy snow", "❄️"),
    77: ("Snow grains", "❄️"),
    80: ("Light rain showers", "🌦️"),
    81: ("Moderate rain showers", "🌦️"),
    82: ("Violent rain showers", "🌧️"),
    85: ("Light snow showers", "🌨️"),
    86: ("Heavy snow showers", "🌨️"),
    95: ("Thunderstorm", "⛈️"),
    96: ("Thunderstorm with small hail", "⛈️"),
    99: ("Thunderstorm with heavy hail", "⛈️"),
}


# Find the best description and emoji for a given weather code from Open-Meteo.
def describe_weather_code(code: int) -> str:
    description, emoji = WEATHER_CODE_DETAILS.get(code, ("Unknown condition", "❓"))
    return f"{emoji} {description}"


# Turn a city name into latitude and longitude coordinates using OpenStreetMap.
def get_coordinates(city_name: str) -> Optional[Tuple[float, float]]:
    geolocator = Nominatim(user_agent="weather-app-tk")
    try:
        location = geolocator.geocode(city_name)
    except GeocoderServiceError:
        messagebox.showerror("Geocoding error", "Geocoding service is unavailable right now.")
        return None

    if not location:
        messagebox.showinfo("City not found", f"Could not find '{city_name}'. Please try another name.")
        return None

    return location.latitude, location.longitude


# Fetch current weather (temperature, humidity, wind, condition) from Open-Meteo.
def fetch_weather(latitude: float, longitude: float) -> Optional[dict]:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
        "hourly": "relativehumidity_2m",
        "timezone": "auto",
    }

    try:
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        messagebox.showerror("Network error", "Cannot reach the weather service right now.")
        return None

    data = response.json()
    current = data.get("current_weather")
    if not current:
        messagebox.showinfo("No data", "The weather provider returned no current weather.")
        return None

    humidity = "N/A"
    hourly = data.get("hourly", {})
    times = hourly.get("time", [])
    humidity_values = hourly.get("relativehumidity_2m", [])
    if current.get("time") in times:
        index = times.index(current["time"])
        if index < len(humidity_values):
            humidity = f"{humidity_values[index]}%"
    elif humidity_values:
        humidity = f"{humidity_values[0]}%"

    return {
        "temperature": f"{current.get('temperature', 'N/A')} °C",
        "windspeed": f"{current.get('windspeed', 'N/A')} km/h",
        "condition": describe_weather_code(current.get("weathercode", -1)),
        "humidity": humidity,
        "time": current.get("time", "Unknown"),
    }


# Draw the main Tkinter window and its widgets for this beginner-friendly app.
class WeatherApp(tk.Tk):
    # Initialize the window, labels, buttons, and layout for the GUI.
    def __init__(self) -> None:
        super().__init__()
        self.title("Accurate Weather Checker")
        self.geometry("420x320")
        self.resizable(False, False)

        tk.Label(self, text="Live weather lookup", font=("Arial", 16, "bold")).pack(pady=(10, 5))
        tk.Label(self, text="Enter a city name and click Search.", font=("Arial", 10)).pack()

        self.city_var = tk.StringVar()
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)
        tk.Entry(entry_frame, textvariable=self.city_var, width=26, font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        tk.Button(entry_frame, text="Search", command=self.search_weather).pack(side=tk.LEFT)

        self.output_var = tk.StringVar()
        self.output_label = tk.Label(
            self,
            textvariable=self.output_var,
            justify=tk.LEFT,
            font=("Consolas", 11),
            anchor="w",
        )
        self.output_label.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)
        self.output_var.set("Your weather summary will appear here.")

    # Respond to the Search button by fetching and displaying the weather for the entered city.
    def search_weather(self) -> None:
        city_name = self.city_var.get().strip()
        if not city_name:
            messagebox.showinfo("Missing city", "Please enter a city name to search.")
            return

        coordinates = get_coordinates(city_name)
        if not coordinates:
            return

        weather = fetch_weather(*coordinates)
        if not weather:
            return

        self.output_var.set(
            f"City: {city_name}\n"
            f"Time: {weather['time']}\n"
            f"Condition: {weather['condition']}\n"
            f"Temperature: {weather['temperature']}\n"
            f"Humidity: {weather['humidity']}\n"
            f"Wind speed: {weather['windspeed']}"
        )


# Start the Tkinter main loop so the user can interact with the GUI.
def main() -> None:
    app = WeatherApp()
    app.mainloop()


if __name__ == "__main__":
    main()
