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

#Looge klass CharCounter. Selle eksemplarile saab lisada sõnu. 
#CharCounter jätab tema sees oleva Adderi kaudu meelde sõnade tähtede koguarvu

class CharCounter:
    def __init__(self, a: Adder):
        self.adder=a
        self.wordadder=None
        
    def setWordAdder(self, a2: Adder):
        self.wordadder=a2
        
    def addWordCharacters(self, word):
        self.adder.add(len(word))
        if self.wordadder: self.wordadder.add(1)
        
    def getCharacterCount(self):
        return self.adder.getSum()
        
    def getWordCount(self):
        if self.wordadder: return self.wordadder.getSum()
        return -1

sa=SimpleAdder()
sa.add(3)
sa.add(2)
print(sa.getSum())

sa2=SimpleAdder()
lugeja1=CharCounter(sa)
lugeja1.setWordAdder(sa2)
lugeja1.addWordCharacters("Juku")
lugeja1.addWordCharacters("Kati")
print(lugeja1.getCharacterCount())
print(lugeja1.getWordCount())

#tee CharCounter klassile käsklus sõnade loendur määramiseks
#juhul, kui loendur on määratud, sellisel juhul suurendatakse iga sõna puhul loendurit ühe võrra
#Küsi loendatud sõnade arv, loenduri puudumisel vastatakse -1
#Kasuta loendmiseks Adderi eraldi eksemplari 

#https://oop2026.jaagupkippar.eu/liides/lisamine2.py
