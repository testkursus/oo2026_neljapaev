class Kolmnurk:
    xid=[]
    yid=[]
    def __init__(self, x1, y1, x2, y2, x3, y3):
       self.xid=[x1, x2, x3]
       self.yid=[y1, y2, y3]

    def __str__(self):
       return ", ".join(["("+str(paar[0])+", "+str(paar[1])+")" for paar in zip(self.xid, self.yid)])

    def tekstiks(self):
        vastus=""
        for nr in range(3):
           vastus+=" ("+str(self.xid[nr])+", "+str(self.yid[nr])+")"
        return vastus

k1=Kolmnurk(1, 3, 2, 4, 3, 5)
print(k1.xid, k1.yid)
k2=Kolmnurk(11, 12, 13, 14, 8, 9)
print(k2)
print(k2.xid, k2.yid)
print(list(zip(k2.xid, k2.yid)))
print(k2.tekstiks())