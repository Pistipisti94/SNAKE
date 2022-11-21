napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

try:
   napI = int(input("Írja be a nap számát (1-7): "))
   print(napok[napI - 1])
except:
   print("Nem jó!")
   