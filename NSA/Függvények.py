import random

t = []
for i in range(5):
    t.append(random.randint(1,100))
print(t)
#Összegzés
o = 0
for x in t:
    o += x
print(o)
#Átlag 
atl=o/len(t)
print(atl)
#Minimum
min=101
for x in t:
    if min > x:
        min = x
print(min)
#Maximum
max=0
for x in t:
    if max < x:
        max = x
print(max)
#Keresés
k=input(int("Ezt keresem: "))
if