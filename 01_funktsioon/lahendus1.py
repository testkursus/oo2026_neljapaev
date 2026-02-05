import urllib.request
fsisu=urllib.request.urlopen("https://www.tlu.ee/~jaagup/andmed/ilm/harkutund.txt").read().decode("utf-8")
#print(fsisu[:100])
andmeread=fsisu.split("\n")[1:]
print(andmeread[0].split(",")[4])