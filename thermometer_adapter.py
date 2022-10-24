from temperature_sensor import TemperatureSensor
from thermometer import Thermometer


class ThermometerAdapter(TemperatureSensor):
    def __init__(self, name, initial_temperature):
        # super(name)
        TemperatureSensor.__init__(self, name)
        self.thermometer = Thermometer(initial_temperature)

    def get_temperature(self):
        return self.thermometer.get_temperature()

    def set_temperature(self, temperature):
        if temperature > self.get_temperature():
            self.thermometer.increase_temperature(temperature - self.get_temperature())
        else:
            self.thermometer.decrease_temperature(self.get_temperature() - temperature)
        super()._notify_temperature_change()