#pip install pillow
from PIL import Image, ImageDraw

pilt1=Image.new("RGB", (200, 200))
g=ImageDraw.ImageDraw(pilt1)
g.rectangle((10, 10, 30, 20)) #x1, y1, x2, y2
g.line((40, 10, 40, 20)) #x1, y1, x2, y2
g.ellipse((10, 30, 30, 40)) #x1, y1, x2, y2  väline kast
g.text((40, 30), "Tere")
pilt1.save("pilt1.gif", "GIF")