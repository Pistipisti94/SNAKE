#Módosítsd a tekn ̋ocös oszlopdiagram rajzoló programot, hogy a 200 és annál nagyobb érték  ̋u oszlopok kitöltésepiros legyen, amelyek értéke a [100 és 200) intervallumban vannak, legyenek sárgák és a 100 alattiak zöldek.
import turtle


def rajzolj_oszlopot(teki, magassag):
    szin(magassag) 
    teki.begin_fill()
    teki.pendown()
    teki.left(90)
    teki.forward(magassag)
    teki.write("  "+ str(magassag))
    teki.right(90)
    teki.forward(40)
    teki.right(90)
    teki.forward(magassag)
    teki.left(90)
    teki.penup()
    teki.forward(20)
    teki.end_fill()
def szin(xs):
    if xs >= 200:
        teki.fillcolor("red")
    elif xs<200 and xs>=100:
        teki.fillcolor("yellow")
    elif xs<=100:
        teki.fillcolor("green")

Scr = turtle.Screen()
Scr.bgcolor("lightgreen")

teki = turtle.Turtle()
teki.color("blue")
teki.pensize(3)

xs = [48,117,200,240,160,260,220]
for m in xs:
    rajzolj_oszlopot(teki, m)
    szin(m)

Scr.mainloop()