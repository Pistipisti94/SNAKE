import turtle

kep = turtle.Screen()
teki = turtle.Turtle()
kep.bgcolor("lightgreen")
teki.pensize("3")
teki.pencolor("blue")
teki.speed(10)

for i in range(0,20):
   teki.forward(100)
   teki.forward(-100)
   teki.left(18)

teki.left(9)
for i in range(0,5):
   teki.penup()
   teki.forward(140)
   teki.left(135)
   teki.pendown()
   for i in range(0,4):
      teki.forward(200)
      teki.left(90)
   teki.penup()
   teki.right(135)
   teki.forward(-140)
   teki.left(18)

teki.forward(200)
kep.mainloop()