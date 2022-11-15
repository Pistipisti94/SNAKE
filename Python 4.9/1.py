import turtle
screen = turtle.Screen()
teki = turtle.Turtle()
screen.bgcolor('lightgreen')
teki.color('hotpink')
teki.pensize('3')

for i in range(4):
    teki.forward(20)
    teki.left(90)

teki.penup()
teki.forward(40)
teki.pendown()

for i in range(4):
    teki.forward(20)
    teki.left(90)

teki.penup()
teki.forward(40)
teki.pendown()

for i in range(4):
    teki.forward(20)
    teki.left(90)

teki.penup()
teki.forward(40)
teki.pendown()

for i in range(4):
    teki.forward(20)
    teki.left(90)

teki.penup()
teki.forward(40)
teki.pendown()




screen.mainloop()