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