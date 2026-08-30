from abc import ABC,abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self,temp,press,humid):
        pass


class Subject(ABC):
    @abstractmethod
    def addObserver(self,observer:Observer):
        pass

    @abstractmethod
    def removeObserver(self,observer:Observer):
        pass

    @abstractmethod
    def notify(self,):
        pass

    @abstractmethod    
    def weathersChanged(self,):
        pass


class Display(ABC):

    @abstractmethod
    def display(self,):
        pass

class Station(ABC):

    @abstractmethod
    def get_temperature(self):
        pass
    @abstractmethod
    def get_pressure(self):
        pass
    @abstractmethod
    def get_humidity(self):
        pass
    @abstractmethod
    def get_forecast(self):
        pass

class WeatherData(Subject):
    
    def __init__(self,station:Station):
        self.observers=set()
        self.station=station

    def addObserver(self, observer:Observer):
        self.observers.add(observer)
    
    def removeObserver(self, observer:Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def weathersChanged(self):
        self.temp=self.station.get_temperature()
        self.press=self.station.get_pressure()
        self.humid=self.station.get_humidity()
        self.forecast=self.station.get_forecast()
        self.notify()



class CurrentDisplayObserver(Observer,Display):
    
    def __init__(self,subject:Subject):
        self.subject=subject
        self.temp=None
        self.press=None
        self.humid=None

    def update(self,):
        self.temp=self.subject.temp
        self.press=self.subject.press
        self.humid=self.subject.humid

    def subscribe(self):
        self.subject.addObserver(self)

    def unsubscribe(self):
        self.subject.removeObserver(self)

    def display(self):
        return f'temp is {self.temp}, press is {self.press}, humidity is {self.humid}'


class ForecastDisplayObserver(Observer,Display):
    
    def __init__(self,subject:Subject,forecast=None):
        self.subject=subject
        self.forecast=None

    def update(self):
        self.temp=self.subject.temp
        self.press=self.subject.press
        self.humid=self.subject.humid
        self.forecast=self.subject.forecast

    def subscribe(self):
        self.subject.addObserver(self)

    def unsubscribe(self):
        self.subject.removeObserver(self)

    def display(self):
        return f'Forecast is {self.forecast}'


class HeatIndexObserver(Observer,Display):
    
    def __init__(self,subject:Subject):
        self.subject=subject
        self.temp=None
        self.press=None
        self.humid=None
        self.heat_index=None

    def update(self):
        self.temp=self.subject.temp
        self.press=self.subject.press
        self.humid=self.subject.humid
        self.heat_index=self.get_heat_index()

    def get_heat_index(self):
        T=self.temp
        RH=self.humid
        return (
                16.923
                + 1.85212e-1 * T
                + 5.37941 * RH
                - 1.00254e-1 * T * RH
                + 9.41695e-3 * T**2
                + 7.28898e-3 * RH**2
                + 3.45372e-4 * T**2 * RH
                - 8.14971e-4 * T * RH**2
                + 1.02102e-5 * T**3
                - 3.8646e-5 * RH**3
                + 2.91583e-5 * T**3 * RH
                + 1.42721e-6 * T**2 * RH**2
                + 1.97483e-7 * T * RH**3
                - 2.18429e-8 * T**3 * RH**2
                + 8.43296e-10 * T**2 * RH**3
                - 4.81975e-11 * T**3 * RH**3
            )

    def subscribe(self):
        self.subject.addObserver(self)

    def unsubscribe(self):
        self.subject.removeObserver(self)

    def display(self):
        return f'HeatIndex is {self.forecast}'


        