#Módosítsd a teknőcös oszlopdiagram rajzoló programot, hogy az oszlopok közti résben a toll fel legyen emelve.
import turtle
def rajzolj_oszlopot(teki, magassag):
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
Scr = turtle.Screen()
Scr.bgcolor("lightgreen")

teki = turtle.Turtle()
teki.color("blue", "red")
teki.pensize(3)

xs = [48,117,200,240,160,260,220]

for m in xs:
    rajzolj_oszlopot(teki, m)
    

Scr.mainloop()