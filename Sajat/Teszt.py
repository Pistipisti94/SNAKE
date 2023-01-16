class game:
    def __init__(self):
        self.champ: str
        self.a:int
        self.s:int
        self.i:int
        self.d:int
        self.end:str
    def karii(self):
            kari = input("Valassz karaktert(ijjasz,harcos,magus): ")
            done = False
            while not done:
                kari = kari.lower()
                if kari == "ijjasz": done = True
                elif kari == "harcos": done = True
                elif kari == "magus": done = True
                if kari == "ijjasz":
                    self.champ = "Ijjász"
                    self.a = 6
                    self.d = 7
                    self.s = 3
                    self.i = 2
                elif kari == "harcos":
                    self.champ = "Harcos"
                    self.a = 7
                    self.d = 4
                    self.s = 8
                    self.i = 1
                elif kari == "magus":
                    self.champ = "Mágus"
                    self.a = 5
                    self.d = 7
                    self.s = 3
                    self.i = 2
                if not done:
                    kari = input("Valassz karaktert(ijjasz,harcos,magus): ")
    

g = game()
g.karii()          
print(g.champ," lettél")