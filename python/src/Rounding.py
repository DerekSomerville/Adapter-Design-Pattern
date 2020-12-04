from abc import ABC, abstractmethod

class Rounding(ABC):

    @abstractmethod
    def round(self,total,count):
        pass
