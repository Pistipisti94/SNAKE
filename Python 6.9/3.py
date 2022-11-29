napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]
print("Írja be egy nap nevét")
napIn = input().lower()
napIndex = None

for i in range(0, len(napok)):
   if napIn == napok[i].lower():
      napIndex = i

print(napIndex)