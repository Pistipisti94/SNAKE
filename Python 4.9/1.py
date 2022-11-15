import turtle
screen = turtle.Screen()
teki = turtle.Turtle()
screen.bgcolor('lightgreen')
teki.color('hotpink')
teki.pensize('3')

class kockak:
    def loop(ennyi):
        for i in range(1):
            teki.forward(20)
            teki.left(90)
            teki.forward(20)
            teki.left(90)
            teki.forward(20)
            teki.left(90)
            teki.forward(20)
            teki.left(90)

    def loop2(annyi):
        for i in range(1):
            teki.penup()
            teki.forward(40)
            teki.pendown()

for i in range(5):
    kockak.loop(1)
    kockak.loop2(1)


screen.mainloop()