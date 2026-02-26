class Kilpkonn:
  suunad={
      "vasakule":[-1, 0],
      "yles":[0, 1],
      "paremale":[1, 0],
      "alla":[0, -1]
    }
  def __init__(self, ux, uy):
    self.x=ux
    self.y=uy
    self.suund="paremale"
    
  def keeraParemale(self):
      #vali päripäeva järgmine suund
      sd=list(Kilpkonn.suunad.keys())
      koht=sd.index(self.suund)
      koht=(koht+1) % 4
      self.suund=sd[koht]
  def edasi(self):
      #Kilpkonn liigub vastavalt suunale ühe sammu edasi
      self.x+=Kilpkonn.suunad[self.suund][0]	
      self.y+=Kilpkonn.suunad[self.suund][1]	
  def liigu(self, sammud):
      #Sammud on string "e" (edasi) ja "p" (paremale) tähtedest
      #Käskluse käivitamisel teeb kilpkonn kõik stringis etteantud sammud 
      for s in sammud: 
           self.edasi() if s=="e" else self.keeraParemale()
  def asukoht(self):
    return str(self.x)+", "+str(self.y)+" "+self.suund
    
  def __str__(self):
      return self.asukoht()
	
k1=Kilpkonn(3, 7)
k1.liigu("eeeeeeepee")
print(k1.asukoht())
print(k1)
k1.edasi()
print(k1)
k1.keeraParemale()
print(k1)
k1.edasi()
print(k1)
