from i_temperature_observer import ITemperatureObserver


class TemperatureAlarm(ITemperatureObserver):
    def update(self, event):
        if event.get_temperature() < 4 or event.get_temperature() > 18:
            print("BIIP BIIP BIIP !!!!!!!!!!")
