import random

f = open("NSA\\prog\\ige.txt","r",encoding="utf-8")
a1 = f.readline()
f.close()
f = open("NSA\\prog\\melleknev.txt","r",encoding="utf-8")
a2 = f.readline()
f.close()
f = open("NSA\\prog\\mgh.txt","r",encoding="utf-8")
a3 = f.readline()
f.close()
ige = a1.split(" ")
melleknev = a2.split(" ")
mgh = a3.split(" ")
nev = input("Ki? ")
hol = input("Hol? ")
ig = ige[random.randint(0,len(ige)-1)]
m1 = melleknev[random.randint(0,len(melleknev)-1)]
m2 = melleknev[random.randint(0,len(melleknev)-1)]
print(m1,nev,ig,m2,hol)