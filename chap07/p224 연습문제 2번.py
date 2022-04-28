import turtle
t=turtle.Turtle()
t.shape("turtle")

def hexagon():
    for i in range(6):
        t.forward(50)
        t.left(360/6)

for i in range(6):
    t.right(60)
    hexagon()
    t.forward(50)



