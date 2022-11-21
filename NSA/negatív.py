x=int(input("Adjon meg egy számot: "))
y=int(input("Adjon meg mégegy számot: "))
if x<0 and y<0:
    print("Mind kettő negatív")
elif x>=0 and y>=0:
    print("Egyik szám sem negatív")
elif x<=0:
    print("Az első szám negatív")
elif y<=0:
    print("A második szám negatív")
