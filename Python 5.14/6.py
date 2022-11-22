jegyek = ["elégtelen","elégséges","közepes","jó","jeles"]
doga = float(input("Pontszám: "))
if doga <60 and doga >=0:
    print(jegyek[0])
elif doga >= 60 and doga <70:
    print(jegyek[1])
elif doga >= 70 and doga <80:
    print(jegyek[2])
elif doga >= 80 and doga <90:
    print(jegyek[3])
elif doga >= 90 and doga <=100:
    print(jegyek[4])

   