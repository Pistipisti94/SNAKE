class hiresek_alap:
    def __init__(self,nev,fog,nemz):
        self.nev = nev
        self.fog = fog
        self.nemz = nemz

    def nemzetiseg(nemz):
        if nemz == "a":
            return "Ms."
        elif nemz == "n":
            return "Frau"
    
t=[]
for x in range(3):
    a=input("Add meg egy híres nő nevét! ")
    b=input("Add meg a foglalkozását! ")
    c=input("Add meg a nemzetiségét (a/n)! ")
    t.append(hiresek_alap(a,b,c))
for x in range(3):
    print(hiresek_alap.nemzetiseg(t[x].nemz),t[x].nev,"egy híres",t[x].fog,)
        

        