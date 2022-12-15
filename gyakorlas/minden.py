from osztaly import *

t1= teglalap()
print("t1 kerület: {0}, területe: {1}".format(t1.getkerulet(),t1.getterulet()))

t1.setA(12)
t1.setB(56)
print(f"A t1 kerülete:: {t1.getkerulet()},területe: {t1.getterulet()}")

t1= negyzet()
print("t1 kerület: {0}, területe: {1}".format(t1.getkerulet(),t1.getterulet()))

t1.setA(12)
print(f"A t1 kerülete:: {t1.getkerulet()},területe: {t1.getterulet()}")

t1= kor()
print("t1 kerület: {0}, területe: {1}".format(t1.getkerulet(),t1.getterulet()))

t1.setR(12)
print(f"A t1 kerülete:: {t1.getkerulet()},területe: {t1.getterulet()}")