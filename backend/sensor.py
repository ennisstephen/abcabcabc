import requests
import sqlite3
from datetime import datetime
import time
import csv


class Sensor:
    def __init__(self, cities):
        self.cities = cities
        self.api_key = "xxxxxxx" #insert https://www.weatherapi.com/ api key here
        self.create_table()
        self.insert_csv("data/weather_data.csv")

    def create_table(self):
        conn = sqlite3.connect("weather_data.db")
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS weather_data")
        c.execute(
            """CREATE TABLE IF NOT EXISTS weather_data
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     region TEXT,
                     temperature REAL,
                     humidity INTEGER,
                     wind_kph REAL,
                     date TEXT)"""
        )
        conn.commit()
        conn.close()

    def insert_csv(self, csv_file):
        conn = sqlite3.connect("weather_data.db")
        c = conn.cursor()

        with open(csv_file, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                region = row["region"]
                temperature = float(row["temperature"])
                humidity = int(row["humidity"])
                wind_kph = float(row["wind_kph"])
                date = row["date"]

                c.execute(
                    """INSERT INTO weather_data 
                             (region, temperature, humidity, wind_kph, date) 
                             VALUES (?, ?, ?, ?, ?)""",
                    (region, temperature, humidity, wind_kph, date),
                )

        conn.commit()
        conn.close()

    def insert_data(self, region, temperature, humidity, wind_kph, date_str):
        conn = sqlite3.connect("weather_data.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO weather_data (region, temperature, humidity, wind_kph, date) VALUES (?, ?, ?, ?, ?)",
            (region, temperature, humidity, wind_kph, date_str),
        )
        conn.commit()
        conn.close()

    def fetch_weather(self, city):
        URL = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}&aqi=no"
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()

            if "current" in data and "location" in data:
                temperature_celsius = data["current"]["temp_c"]
                humidity = data["current"]["humidity"]
                wind_kph = data["current"]["wind_kph"]
                region = data["location"]["region"]

                current_date = datetime.now().date().isoformat()

                self.insert_data(
                    region, temperature_celsius, humidity, wind_kph, current_date
                )

                print(f"Data saved to SQLite for {city}.")
            else:
                print(f"No current weather or location data available for {city}.")
        else:
            print(
                f"Error fetching data for {city}. Status code: {response.status_code}"
            )

    def fetch_and_save_weather(self):
        while True:
            for city in self.cities:
                self.fetch_weather(city)
                time.sleep(60)
