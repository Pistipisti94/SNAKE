
def testmagassag(ma):
    if ma>170:
        return True
    else:
        return False

nev = input("Név: ")
while(nev!=""):
    m = int(input("Magassag(CM): "))
    if testmagassag(m):
        print(nev," magasabb mint az átlag!")
    else:
        print(nev," nem magasabb mint az átlag!")
    nev = input("Név: ")