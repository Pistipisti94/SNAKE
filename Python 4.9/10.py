import turtle

kep = turtle.Screen()
teki = turtle.Turtle()
kep.bgcolor("lightgreen")
teki.pensize("3")
teki.pencolor("hotpink")
teki.speed(10)

teki.left(35)
for i in range(0,5):
   for i in range(0,5):
      teki.forward(100)
      teki.left(144)
   teki.penup()
   teki.forward(650)
   teki.right(144)
   teki.pendown()

kep.clear()
kep = turtle.Screen()
teki = turtle.Turtle()
kep.bgcolor("lightgreen")
teki.pensize("3")
teki.pencolor("hotpink")

teki.left(35)
for i in range(0,5):
   for i in range(0,5):
      teki.forward(100)
      teki.left(144)
  
   teki.forward(650)
   teki.right(144)
  

kep.mainloop()

