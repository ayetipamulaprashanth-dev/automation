import requests
import pandas as pd

# 1. Ask the API for data
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 51.51,
    "longitude": -0.13,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Europe/London",
}
response = requests.get(url, params=params, timeout=10)
response.raise_for_status()  # stop with an error if the request failed

# 2. Read the JSON reply
data = response.json()["daily"]

# 3. Turn it into a table
df = pd.DataFrame({
    "Date": data["time"],
    "Max temp (°C)": data["temperature_2m_max"],
    "Min temp (°C)": data["temperature_2m_min"],
    "Rain (mm)": data["precipitation_sum"],
})

# 4. Save it to Excel
df.to_excel("london_weather.xlsx", index=False)
print(df)
print("Saved to london_weather.xlsx")