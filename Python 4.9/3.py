import turtle

kep = turtle.Screen()
teki = turtle.Turtle()
kep.bgcolor("lightgreen")
teki.pensize("3")
teki.pencolor("hotpink")

def sokszog_rajzolas(t,n,sz):
   for i in range(0,n):
      teki.left(sz)
      teki.forward(50)


sokszog_rajzolas(teki, 8, 45)

kep.mainloop()