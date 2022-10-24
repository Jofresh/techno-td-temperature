class Thermometer:
    def __init__(self, initial_temperature):
        self.temperature = initial_temperature

    def increase_temperature(self, value):
        self.temperature += value + 0.1;

    def decrease_temperature(self, value):
        self.temperature -= value + 0.1

    def get_temperature(self):
        return self.temperature