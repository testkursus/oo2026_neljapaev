import math
class Hulknurk:
    xid=[]
    yid=[]
    def __init__(self, x1, y1, x2, y2, x3, y3):
       self.xid=[x1, x2, x3]
       self.yid=[y1, y2, y3]

    def lisa(self, x, y):
       self.xid.append(x)
       self.yid.append(y)

    def ymbermoot(self):
      v=0
      for nr in range(len(self.xid)):
         dx=self.xid[(nr+1) % len(self.xid)]-self.xid[nr]
         dy=self.yid[(nr+1) % len(self.xid)]-self.yid[nr]
         v+=math.sqrt(dx*dx+dy*dy)
      return v
    
    def paremale(self):
        for nr in range(len(self.xid)):
            self.xid[nr]+=1

    def p2(self):
        self.xid=[x+1 for x in self.xid]

    def p2a(self):
        uus=[]
#        for x in self.xid: uus.append(x+1)
        for nr in range(len(self.xid)):uus.append(self.xid[nr])
        self.xid=uus

    def nihuta(self, dx, dy):
        for nr in range(len(self.xid)):
            self.xid[nr]+=dx
            self.yid[nr]+=dy

    def n2(self, dx, dy):
        self.xid=[x+dx for x in self.xid]
        self.yid=[y+dy for y in self.yid]

    def suurenda(self, tegur):
         for nr in range(len(self.xid)):
            self.xid[nr]*=tegur
            self.yid[nr]*=tegur       

k1=Hulknurk(1, 3, 2, 0, 3, 5)
print(k1.xid)
k1.suurenda(2)
print(k1.xid)
k1.paremale()
print(k1.xid)
k1.nihuta(-2, -1)
print(k1.xid)
k1.p2()
print(k1.xid)
print(k1.ymbermoot())
k1.lisa(2, 8)
print(k1.ymbermoot())
