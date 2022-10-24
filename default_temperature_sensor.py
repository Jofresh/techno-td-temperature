from temperature_sensor import TemperatureSensor


class DefaultTemperatureSensor(TemperatureSensor):
    def __init__(self, name):
        # super(name)
        TemperatureSensor.__init__(self, name)
        self.temperature = 0

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        self._notify_temperature_change()
