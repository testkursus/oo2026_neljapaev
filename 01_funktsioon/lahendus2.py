import urllib.request
fsisu=urllib.request.urlopen("https://www.tlu.ee/~jaagup/andmed/ilm/harkutund.txt").read().decode("utf-8")
andmeread=fsisu.split("\n")[1:]
andmeread=[rida.strip().split(",") for rida in andmeread]
#print(andmeread[-5:])
jaanuarisademed=sum([float(rida[3]) for rida in andmeread if rida[0]=="1"])
print(jaanuarisademed)

def kuusademed(kuunr):
    return sum([float(rida[3]) for rida in andmeread if rida[0]==str(kuunr)])

print(kuusademed(8))
print([kuusademed(knr) for knr in range(1, 13)])