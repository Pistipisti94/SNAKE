napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]
innap = int(input("Melyik nap indultál(1-7) "))
oda = int(input("Hány napig voltál oda? "))
for i in range(1, oda):
   if innap != 6:
      innap += 1
   else:
      innap = 0

print(f"{napok[innap]}i napon jössz haza.")