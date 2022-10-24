from weather_station import WeatherStation
from temperature_alarm import TemperatureAlarm
from default_temperature_sensor import DefaultTemperatureSensor
from thermometer_adapter import ThermometerAdapter


if __name__ == '__main__':
    ws1 = WeatherStation()
    ws2 = WeatherStation()
    ta = TemperatureAlarm()

    ts1 = DefaultTemperatureSensor("Salon")
    ts2 = DefaultTemperatureSensor("Cave")
    ts3 = ThermometerAdapter("Jardin", 4)

    ts1.add_observer(ws1)
    ts1.add_observer(ws2)
    ts2.add_observer(ws2)
    ts3.add_observer(ws2)
    ts2.add_observer(ta)

    print("Salon 20°, Cave 14°, Jardin 19°")
    ts1.set_temperature(20)
    ts2.set_temperature(14)
    ts3.set_temperature(19)
    print("Jardin 13°")
    ts3.set_temperature(13)
    print("Salon 19°")
    ts2.set_temperature(3)
