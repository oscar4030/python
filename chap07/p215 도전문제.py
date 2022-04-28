import turtle
t=turtle.Turtle()

def circle(length):
    t.circle(length)
    t.left(90)

def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color("green")
    circle(50)
    t.end_fill()

    s = turtle.Screen()
    s.onscreenclick(drawit)

turtle.done()