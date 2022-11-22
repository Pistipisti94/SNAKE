jegyek = ["elégtelen","elégséges","közepes","jó","jeles"]
doga = float(input("Pontszám: "))

def Értékelés(pont):
    jegy = 0
    if doga <60 and doga >=0:
        jegy = 0
    elif doga >= 60 and doga <70:
       jegy = 1
    elif doga >= 70 and doga <80:
        jegy = 2
    elif doga >= 80 and doga <90:
        jegy = 3
    elif doga >= 90 and doga <=100:
        jegy = 4
    return jegy

print(jegyek[Értékelés(doga)])