# Weather data class
class WeatherData:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def measurements_changed(self):
        # Notify observers about the state change
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)