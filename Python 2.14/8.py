Nido = int(input("Írd be a jelenlegi időt: "))
csengetes_ido = int(input("Írd be hány óra múlva csörögjön az óra: "))

for i in range(0, csengetes_ido):
   if Nido == 23:
      Nido = 0
   else:
      Nido += 1

print("Az óra",Nido,"órakkor fog megszólalni!")
