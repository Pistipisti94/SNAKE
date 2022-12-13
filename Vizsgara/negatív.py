x=int(input("Adj meg egy számot! "))
y=int(input("Add meg a második számot! "))
if x<0 and y<0:
    print("Mind a két szám negatív")
elif x>=0 and y>=0:
    print("Egyik szám sem negatív")
elif x<=0:
    print("Az első szám negatív")
elif y<=0:
    print("A második szám negatív")
