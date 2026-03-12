from abc import ABC, abstractmethod
import datetime

class Adder(ABC):
    @abstractmethod
    def add(self, nr: float) -> None:
        pass

    @abstractmethod
    def getSum(self) -> float:
        pass     

    def greet(self) -> None:
       print("hello")  
       
       
class FileStoringAdder(Adder):
    def __init__(self, failinimi):
         self.failinimi=failinimi
         
    def add(self, nr: float) -> None:
       with open(self.failinimi, "a") as f2:
           print(nr, datetime.datetime.now().strftime("%X"), sep=",", file=f2)
           
    def getSum(self):
        return sum([float(rida.split(",")[0]) for rida in open(self.failinimi).readlines()])



        
a:Adder=FileStoringAdder("arvud1.txt")
a.add(7)
a.add(11)
a.greet()
print(a.getSum())