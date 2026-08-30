from weather import Station,WeatherData,CurrentDisplayObserver
import numpy as np

class NewStation(Station):

    def get_temperature(self):
        return np.random.randint(10,20)
    def get_pressure(self):
            return np.random.randint(100,200)
    def get_humidity(self):
            return np.random.randint(80,90)

def test_station_is_able_to_update_weatherdata_and_observer():
    new_station=NewStation()
    new_weather_data=WeatherData(new_station)
    new_observer=CurrentDisplayObserver(new_weather_data)

    new_observer.subscribe()
    new_weather_data.weathersChanged()

    assert new_weather_data.temp>=10 and new_weather_data.temp<20 and new_observer.temp==new_weather_data.temp

def test_when_observer_subscribes_then_only_it_receives_updates():
    new_station=NewStation()
    new_weather_data=WeatherData(new_station)
    new_observer=CurrentDisplayObserver(new_weather_data)

    new_weather_data.weathersChanged()

    assert new_weather_data.temp>=10 and new_weather_data.temp<20 and new_observer.temp is None


def test_when_observer_unsubscribes_it_is_no_loger_able_to_get_updates():
    new_station=NewStation()
    new_weather_data=WeatherData(new_station)
    new_observer=CurrentDisplayObserver(new_weather_data)

    new_observer.subscribe()

    new_weather_data.weathersChanged()

    assert new_weather_data.temp>=10 and new_weather_data.temp<20 and new_observer.temp==new_weather_data.temp
    new_observer.unsubscribe()
    assert new_observer not in new_weather_data.observers
    new_weather_data.weathersChanged()
    assert new_observer.temp!=new_weather_data.temp