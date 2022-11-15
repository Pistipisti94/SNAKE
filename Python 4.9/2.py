import turtle

kep = turtle.Screen()
teki = turtle.Turtle()
megy = 20
kep.bgcolor("lightgreen")
teki.pensize("3")
teki.pencolor("hotpink")
class kockak:
   def Rajzol():
      teki.pendown()
      for i in range(0,4):
         teki.left(90)
         teki.forward(megy)
      teki.penup()
      
   def New():
      for i in range(0,2):
         teki.forward(10)
         teki.right(90)
      teki.right(180)

for i in range(0,5):
   kockak.Rajzol()
   kockak.New()
   megy += 20

kep.mainloop()