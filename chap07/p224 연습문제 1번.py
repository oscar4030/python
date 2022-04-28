import turtle
t=turtle.Turtle
t.shape("turtle")
s=turtle.Screen()
s.bgcolor('skyblue')
t.color('black','white')

def draw_snowman(x,y):
    t.up()
    t.goto(x,y+100)
    t.down()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.up()
    t.goto(x,y+70)
    t.down()
    t.left(25)
    t.forward(70)
    t.forward(-70)
    t.left(110)
    t.forward(80)
    t.forward(-80)
    t.seth(0)
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.up() 
    t.goto(x,y)
    t.down() 
    t.begin_fill() 
    t.circle(40) 
    t.end_fill()
for i in range(3): 
    draw_snowman(200*i-200,0)