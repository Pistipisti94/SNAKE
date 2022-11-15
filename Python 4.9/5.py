import turtle

kep = turtle.Screen()
teki = turtle.Turtle()
teki.speed(50)
hossz = 1
kep.bgcolor("lightgreen")
teki.pensize("3")
teki.pencolor("blue")

for i in range(0, 100):
   teki.forward(hossz)
   teki.right(90)
   hossz += 5


kep.clear()
teki = turtle.Turtle()
szög = 91
hossz = 10
teki.speed(50)
kep.bgcolor("lightgreen")
teki.pensize("3")
teki.pencolor("blue")

for i in range(0, 100):
   teki.forward(hossz)
   teki.left(szög)
   hossz += 5

kep.mainloop()