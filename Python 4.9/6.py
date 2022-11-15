import turtle

def rajz(teki, sz):
   n = 360/sz
   for i in range(0,int(n)):
      teki.forward(300)
      teki.left(sz)

kep = turtle.Screen()
teki = turtle.Turtle()
kep.bgcolor("lightgreen")
teki.pensize("6")
teki.pencolor("blue")

rajz(teki, 120)

kep.mainloop()