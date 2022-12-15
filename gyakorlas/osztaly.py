class teglalap:
    def __init__(self,a=0,b=0):
        self.a = a
        self.b = b
    def setA(self, a):
        self.a = a
    def setB(self, b):
        self.b = b
    def setAB(self,a, b):
        self.b = b
        self.a = a
    def getA(self):
        return self.a
    def getkerulet(self):
        return 2*(self.a)+(self.b)
    def getterulet(self):
        return (self.a)*(self.b)

class negyzet:
    def __init__(self,a=0):
        self.a = a
    def setA(self,a):
        self.a = a
    def getA(self):
        return self.a
    def getkerulet(self):
        return 4*(self.a)
    def getterulet(self):
        return (self.a)*(self.a)

class kor:
    def __init__(self,r=0,):
        self.r=r
    def setR(self, r):
        self.r = r
    def getR(self):
        return self.r
    def getkerulet(self):
        return 2*(self.r)*3.14
    def getterulet(self):
        return ((3.14*(2*self.r))/4) 

class hasab:
    def __init__(self,a = 0,m = 0,b = 0):
        self.a = a
        self.m = m
        self.b = b
    def setA(self,a):
        self.a = a
    def setM(self,m):
        self.m = m
    def setB(self,b):
        self.b = b
    def getA(self):
        return self.a
    def getM(self):
        return self.m
    def getB(self):
        return self.b
    def getfelulet(self):
        return (self.a*self.b+self.a*self.m+self.b*self.m)*2
    def getterfogat(self):
        return (self.a*self.b*self.m)

class valaki:
    def __init__(self,nev="",kora=0,nem=""):
        self.nev=nev
        self.kor=kora
        self.nem=nem
    def setnev(self,nev):
        self.nev=nev
    def setkor(self,kora):
        self.kora= kora
    def setnem(self,nem):
        self.nem=nem
    def getnev(self):
        return self.nev
    def getkor(self):
        return self.kora
    def getnem(self):
        return self.nem
