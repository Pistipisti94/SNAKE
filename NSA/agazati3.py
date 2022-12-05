import random

class szere:
    def __init__(self,nev,fog,nem,szsz):
        self.nev = nev
        self.fog = fog
        self.nem = nem
        self.szsz = szsz

    def FvN(nem):
        if nem == "f" :
            return "férfi"
        elif nem == "n" :
            return "nő"

t=[]
for x in range(3):
    a=input("Add meg a neved: ")
    b=input("Add meg a foglalkozásod: ")
    c=input("Add meg a nemed (f/n): ")
    d=random.randint(1,50)
    t.append (szere(a,b,c,d))
for x in range(3):
    print(t[x.nev,""])