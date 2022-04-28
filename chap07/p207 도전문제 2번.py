import turtle

t=turtle.Turtle()
t.shape("turtle")

colorList =["red","blue","green"]

def square(length,index):
    t.color(colorList[index])
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()


t.up()
t.goto(-200,0)
t.down()
square(100,0)

t.up()
t.goto(0,0)
t.down()
square(100,1)

t.up()
t.goto(200,0)
t.down()
square(100,2)