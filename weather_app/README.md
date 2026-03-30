# Weather App with Tkinter

This version replaces the console loop with a simple Tkinter window that lets you type a city name, click **Search**, and immediately see the temperature, humidity, wind speed, and a condition line with an emoji pulled from Open-Meteo.

## What it does

- Uses `geopy` to convert the typed city into coordinates.
- Calls Open-Meteo (`WEATHER_API_URL`) for current weather and humidity data.
- Displays everything in a friendly GUI with easy-to-read labels and emojis.
- Handles missing cities and network problems with pop-up dialogs.

## Installation

1. Open a terminal inside the `weather_app` folder.
2. Install the required libraries:

```bash
python -m pip install requests geopy
```

3. Tkinter is shipped with most Python 3 installations; no extra package is needed.

## Running the app

Run the window with:

```bash
python weather_app.py
```

Type a city name (e.g., `Seoul`), then click **Search**. The window updates with the latest data or displays helpful messages if something goes wrong.

## Screenshot

![Screenshot placeholder](screenshot.png)
