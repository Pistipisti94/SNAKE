import random

class Ember:
    def __init__(self,nev,fog,nem,szsz):
        self.nev = nev
        self.fog = fog
        self.nem = nem
        self.szsz = szsz

    def AvN(nem):
        if nem == "a" :
            return "mr"
        elif nem == "n" :
            return "frau"

t=[]
for x in range(1):
    a=input("Add meg a neved: ")
    b=input("Add meg a foglalkozásod: ")
    c=input("Add meg a nemed (a/n): ")
    d=random.randint(1,50)
    t.append(Ember(a,b,c,d))
for x in range(1):
    print(t[])