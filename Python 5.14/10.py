#Írj egyatfogofüggvényt, amely megkapja egy derékszög  ̋u háromszög két befogójának a hosszát és visszaadjaaz átfogó hosszát! (Segítség: azx**0.5a négyzetgyököt adja vissza.)

egy = 0
ketto = 0

isDone = True
while isDone:
   try:
      egy = int(input("Írja be az első befogót hosszát (cm): "))
      ketto = int(input("Írja be a második befogót hosszát (cm): "))
      isDone = False
   except:
      print("Rossz adatbevitel!")

print(f"A derkészögű háromszög átfogója {(((egy*egy) + (ketto*ketto)) ** 0.5)}cm.")
