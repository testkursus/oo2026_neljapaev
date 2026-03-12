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

class CharCounter:
    def __init__(self, a: Adder):
        self.adder=a
        
    def addWordCharacters(self, word):
        self.adder.add(len(word))
        
    def getCharacterCount(self):
        return self.adder.getSum()
        

        
a:Adder=FileStoringAdder("sonapikkused.txt")
c:CharCounter=CharCounter(a)
sisend=input("Palun lause, katkestuseks enter: ")
while sisend:
  for sona in sisend.split(): c.addWordCharacters(sona)
  sisend=input("Palun lause, katkestuseks enter: ")
    
print(a.getSum())