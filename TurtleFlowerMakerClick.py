import turtle as t
from itertools import cycle

colors = cycle(['violet','pink','cyan','white','red','orange','yellow','green','blue','purple'])

t.clear()
t.bgcolor('black')
t.speed(100)
t.pensize(10)

def draw_flower(x,y):
    t.up()
    t.pencolor(next(colors))
    t.goto(x,y)
    t.setheading(0)
    t.down()
    for i in range(5):
        for i in range(35):
            t.forward(3)
            t.right(3)
        t.right(75)
        for i in range(35):
            t.forward(3)
            t.right(3)
    
t.onscreenclick(draw_flower)

