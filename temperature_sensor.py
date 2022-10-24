from temperature_change_event import TemperatureChangeEvent
from i_temperature_observer import ITemperatureObserver

import abc


# abstract class

class TemperatureSensor(abc.ABC):
    def __init__(self, name):
        self.__name = name
        self.__temperature = 0
        self.__observers = []

    @abc.abstractmethod
    def get_temperature(self):
        pass

    @abc.abstractmethod
    def set_temperature(self, temperature):
        pass

    def add_observer(self, o: ITemperatureObserver):
        self.__observers.append(o)

    def _notify_temperature_change(self):
        e = TemperatureChangeEvent(self.get_temperature(), self.__name)
        for o in self.__observers:
            o.update(e)
