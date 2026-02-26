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


k1=Hulknurk(1, 3, 2, 0, 3, 5)
print(k1.ymbermoot())
k1.lisa(2, 8)
print(k1.ymbermoot())
