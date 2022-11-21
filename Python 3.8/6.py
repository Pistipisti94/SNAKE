import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()

def Ki(hanyszor, fok):
   screen.clear()
   teknos = turtle.Turtle()
   for i in range(0, hanyszor):
      teknos.left(fok)
      teknos.forward(100)

Ki(3,120)
Ki(4,90)
Ki(6,60)
Ki(8,45)

screen.mainloop()