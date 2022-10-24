import abc


class ITemperatureObserver(abc.ABC):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return hasattr(subclass, 'update') and callable(subclass.update) or NotImplemented

    @abc.abstractmethod
    def update(self, event):
        raise NotImplementedError
