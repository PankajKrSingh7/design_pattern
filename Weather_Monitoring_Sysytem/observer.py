from abc import ABC, abstractmethod
# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass