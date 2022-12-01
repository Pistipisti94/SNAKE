def egy(szam):
    if szam/3600:
        return True
    else:
        return False
be = int(input("Másodperc-óra(mp): "))
if egy(be):
    print(be,"másodperc az ",int(be/3600),"óra")
else:
    print(be,"másodperc az ",int(be/3600), "óra")

def ketto(szamm):
    if szamm/60:
        return True
    else:
        return False
bee = int(input("Másodperc-perc(mp): "))
if egy(bee):
    print(bee," másodperc az ",int(bee/60),"perc")
else:
    print(bee," másodperc az ",int(bee/60),"perc")
def ketto(szammm):
    if szammm%60==0:
        return True
    else:
        return False
beee = int(input("Másodperc/perc-maradék másodperc(mp): "))
if egy(beee):
    print(beee," másodpercbe ",int(beee%60),"maradék másodperc van")
else:
    print(beee," másodpercbe ",int(beee%60),"maradék másodperc van")

