from weather_data import WeatherData

# Weather station class
class WeatherStation:
    def __init__(self):
        self.weather_data = WeatherData()
        self.weather_data.observers = []

    def add_observer(self, observer):
        # Add observer to the list of observers
        self.weather_data.observers.append(observer)

    def remove_observer(self, observer):
        # Remove observer from the list of observers
        self.weather_data.observers.remove(observer)

    def update_weather_data(self, temperature, humidity, pressure):
        # Update weather data and notify observers
        self.weather_data.set_measurements(temperature, humidity, pressure)