import math
class Hulknurk:
  def __init__(self, x0, y0, n, r):
     self.x0=x0
     self.y0=y0
     self.n=n
     self.r=r 
  def koordinaadid(self):
     v=[]
     for nr in range(self.n):
       nurk=nr*6.28/self.n
       x=math.cos(nurk)*self.r+self.x0
       y=math.sin(nurk)*self.r+self.y0	 
       v.append([x, y])
     return v
     
  def pindala(self):
      return self.r*self.r*math.sin(6.28/self.n)*self.n/2
     
h1=Hulknurk(1, 2, 3, 5)
print(h1.koordinaadid())
print(h1.pindala())
