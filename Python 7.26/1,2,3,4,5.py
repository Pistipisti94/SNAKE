def paratlan():
    t=[1,2,3,4,5,6,7,8,9,10,11,12,13,1,1,1,1,1,1]
    paratlan=0
    for x in t:
        if x%2==1:
            paratlan=paratlan+1
    print(paratlan)
paratlan()

def osszead():
    t=[1,2,3,4,5,6,7,8,9,10,11,12,13,1,1,1,1,1,1]
    paros=0
    for x in t:
        if x%2==0:
            paros=paros+x
    print(paros)
osszead()

def negativ():
    t=[-1,-2,3,-4,5,6,7,8,-9,10,11,12,-13,1,1,1,1,1,1]
    bt=[]
    for x in t:
        if x<0:
            bt.append(x)
    print(bt)
negativ()

def otszo():
    t=["szo","szavak","otbet","ferko"]
    a=0
    for i in t:
        x = len(i)
        if x == 5:
            a += 1
    print(a)
otszo()

def paroselott():
    t=[1,3,5,7,-2,9,2,4,6,8,1,4,5,7,1,2,9]
    bt=[]
    for x in t:
        if x%2!=0:
            bt.append(x)
        else:
            return bt
    
print(paroselott())

def paroselott():
    t=[1,3,5,7,]
    bt=[]
    for x in t:
        if x%2!=0:
            bt.append(x)
        else:
            return bt
    
print(paroselott())
#Azt írja None
