class konyv:
    def __init__(self,cim,oldalszam,mufaj):
        self.cim = cim
        self.oldalszam = oldalszam
        self.mufaj = mufaj

print("Könybebebevevőőő")
q=konyv(input("Cím: "),int(input("Oldalak száma: ")),input("Műfaj: "))
print(q.cim)
print(q.oldalszam)
print(q.mufaj)
