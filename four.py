from turtle import *
from colorsys import *
speed(0)
bgcolor('black')
h=0
for i in range(100):
    h+=0.0018
    color(hsv_to_rgb(h, 1, 1))
    goto(0,0)
    circle(50,100)
    fd(i)
    rt(80)
    fd(60)
    rt(80)
    hideturtle()
done()    