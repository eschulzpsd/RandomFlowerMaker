from turtle import *
import random
from itertools import cycle

colors = cycle(['violet','pink','cyan','white','red','orange','yellow','green','blue','purple'])


clear()
bgcolor('black')
speed(100)
pensize(10)
up()

for i in range(10):
    randomx = random.randint(-200,200)
    randomy = random.randint(-200,200)
    print(randomx, randomy)
    pencolor(next(colors))
    draw_flower(randomx,randomy)
    up()

def draw_flower(xstart,ystart):
    goto(xstart,ystart)
    setheading(0)
    down()
    for i in range(5):
        for i in range(35):
            forward(3)
            right(3)
        t.right(75)
        for i in range(35):
            t.forward(3)
            t.right(3)
        
    


