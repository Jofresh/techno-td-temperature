from i_temperature_observer import ITemperatureObserver


class WeatherStation(ITemperatureObserver):
    station_counter = 0

    def __init__(self):
        WeatherStation.station_counter = WeatherStation.station_counter + 1
        self.__number = WeatherStation.station_counter

    def update(self, event):
        print(f'Station {self.__number} - {event.get_sensor_name()} {event.get_temperature()}°')
