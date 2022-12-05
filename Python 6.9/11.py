def osszehasonlitas(x,y):
    h=0
    if x>y:
        print("1")
    elif x<y:
        print("-1")
    elif x==y:
        print("0")
    return h
a=int(input("Szám1: "))
b=int(input("Szám2: "))
osszehasonlitas(a,b)
