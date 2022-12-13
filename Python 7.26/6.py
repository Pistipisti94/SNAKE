def szonez():
    t = ["asd","ferike","igen","nem","asd","ferike","igen","nem"]
    a = 0
    for x in t:
        if x !="nem":
            a = a + 1
        else:
            a = a + 1
            return a
    
print(szonez())

def szonez2():
    t = ["asd","ferike","igen","asd","ferike","igen"]
    a = 0
    for x in t:
        if x !="nem":
            a = a + 1
        else:
            a = a + 1
            return a
    
print(szonez2())