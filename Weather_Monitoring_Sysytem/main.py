from weather_station import WeatherStation
from display_devices import MobileAppDisplay
from display_devices import DesktopApplicationDisplay
from display_devices import WebInterfaceDisplay

weather_station = WeatherStation()

mobile_app_display = MobileAppDisplay()
web_interface_display = WebInterfaceDisplay()
desktop_app_display = DesktopApplicationDisplay()

# Add display devices as observers
weather_station.add_observer(mobile_app_display)
weather_station.add_observer(web_interface_display)
weather_station.add_observer(desktop_app_display)

# Update weather data
weather_station.update_weather_data(25, 60, 1013)

# Remove a display device
weather_station.remove_observer(mobile_app_display)

# Update weather data
weather_station.update_weather_data(30, 50, 1201)

# Update weather data again
weather_station.update_weather_data(23, 55, 1009)