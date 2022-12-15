from osztaly import hasab

t1= hasab()
print("t1 felülete: {0}, térfogata: {1}".format(t1.getfelulet(),t1.getterfogat()))

t1.setA(12)
t1.setM(10)
t1.setB(20)
print(f"A t1 felülete:: {t1.getfelulet()},térfogata: {t1.getterfogat()}")