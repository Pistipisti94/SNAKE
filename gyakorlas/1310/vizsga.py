def pont(pts):
    if pts>=48:
        print(nev,"vizsgája sikeres")
    else:
        print(nev,"vizsgája sikertelen.")

nev = input("Add meg a vizsgázó nevét! ")
while nev != "":
    szam = int(input("Add meg a pontszámát! "))
    pont(szam)
    nev = input("Add meg a vizsgázó nevét! ")