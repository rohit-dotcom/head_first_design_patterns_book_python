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
    
    def __init__(self,subject:Subject,temp=None,press=None,humid=None):
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
        self.forecast=self.subject.forecast

    def subscribe(self):
        self.subject.addObserver(self)

    def unsubscribe(self):
        self.subject.removeObserver(self)

    def display(self):
        return f'Forecast is {self.forecast}'



        