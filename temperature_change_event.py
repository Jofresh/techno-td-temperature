class TemperatureChangeEvent:
    def __init__(self, temperature, sensor_name):
        self.__sensor_name = sensor_name
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

    def get_sensor_name(self):
        return self.__sensor_name
