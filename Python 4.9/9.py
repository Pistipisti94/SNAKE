import turtle

kep = turtle.Screen()
teki = turtle.Turtle()
kep.bgcolor("lightgreen")
teki.pensize("3")
teki.pencolor("black")

teki.left(35)
for i in range(0,5):
   teki.forward(200)
   teki.left(144)

kep.mainloop()