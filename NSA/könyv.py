def long(a):
    b=False
    if a>150:
        b=True
    return b

x=input("Add meg a könyv címét: ")
while(x!=""):
    y=int(input("Add meg az oldalszámot: "))
    old=long(y)
    if old:
        print("A köny hosszú")
    else:
        print("A könyv rövid")
