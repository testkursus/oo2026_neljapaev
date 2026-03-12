from abc import ABC, abstractmethod

class Adder(ABC):
    @abstractmethod
    def add(self, nr: float) -> None:
        pass

    @abstractmethod
    def getSum(self) -> float:
        pass     

    def greet(self) -> None:
       print("hello")        
       
#Looge Adder-i alamklass SimpleAdder
#Defineerige meetodid lisamiseks ja summa leidmiseks

class SimpleAdder(Adder):
    def __init__(self):
        self.total=0
        
    def add(self, nr:float) -> None:
        self.total+=nr
        
    def getSum(self) -> float:
        return self.total

#Katsetage tulemust       
#a=Adder()
sa=SimpleAdder()
sa.add(3)
sa.add(2)
print(sa.getSum())