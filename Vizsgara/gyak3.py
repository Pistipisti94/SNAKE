class Hireseg:
    def __init__(self,nev,fog,nemz):
        self.nev = nev
        self.fog = fog
        self.nemz = nemz

    def AvN(nemz):
        if nemz == "a" :
            return "Ms."
        elif nemz == "n" :
            return "Frau"
 
t = []

for x in range(1):
    a = input("Add meg egy híres nő nevét! ")
    b = input("Add meg a foglalkozását! ")
    c = input("Add meg a nemzetiségét!(a/n) ")
    t.append(Hireseg(a,b,c))
for x in t:
    print(x.nemz, x.nev, x.fog)