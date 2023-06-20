from observer import Observer

# Display device classes
class MobileAppDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        # Update mobile app interface with new weather data
        print(f"Mobile App Display: Temperature {temperature}°C, Humidity {humidity}%, Pressure {pressure}hPa")

class WebInterfaceDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        # Update web interface with new weather data
        print(f"Web Interface Display: Temperature {temperature}°C, Humidity {humidity}%, Pressure {pressure}hPa ")

class DesktopApplicationDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        # Update desktop application interface with new weather data
        print(f"Desktop Application Display: Temperature {temperature}°C, Humidity {humidity}%, Pressure {pressure}hPa")