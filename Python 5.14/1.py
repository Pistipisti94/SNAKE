napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

try:
   napI = int(input("Írja be a nap számát (0-6): "))
   print(napok[napI])
except:
   print("Nem jó!")
   