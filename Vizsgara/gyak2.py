def vizsga(a):
    if a >= 100:
        return True
    else:
        return False

a = input("Add meg a vizsgázó nevét! ")        
while (a != ""):
    b = int(input("Add meg a pontszámát! "))
    if vizsga(b):
        print(a," vizsgája sikeres.")
    else:
        print(a," vizsgája sikertelen.")
    a = input("Add meg a vizsgázó nevét! ")    
