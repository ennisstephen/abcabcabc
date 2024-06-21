from backend.sensor import Sensor
from backend.app import app
import threading

if __name__ == "__main__":
    cities = ["Galway", "Dublin", "Cork"]  # Add more cities as needed

    sensor = Sensor(cities)
    weather_thread = threading.Thread(target=sensor.fetch_and_save_weather)
    weather_thread.start()

    flask_thread = threading.Thread(target=app.run(host="0.0.0.0", port=5000))
    flask_thread.start()
