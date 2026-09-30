from __future__ import annotations
from abc import ABC,abstractmethod

class BeatsModelInterface(ABC):
    @abstractmethod
    def initialize():
        pass
    @abstractmethod
    def on():
        pass
    @abstractmethod
    def off():
        pass
    @abstractmethod
    def setBPM():
        pass
    @abstractmethod
    def registerObserver(BeatObserver):
        pass
    @abstractmethod
    def removeObserver(BeatObserver):
        pass
    @abstractmethod
    def  registerObserver(BPMObserver):
        pass
    @abstractmethod
    def removeObserver(BPMObserver):
        pass