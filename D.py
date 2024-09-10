import turtle

from turtle import Turtle
import time

pen = Turtle()

pen.speed(1000)
pen.fillcolor("red")
pen.begin_fill()
pen.left(140)
pen.forward(113)

for i in range(200):
    pen.right(1)
    pen.forward(1)

pen.left(120)

for i in range(200):
    pen.right(1)
    pen.forward(1)

pen.forward(112)
pen.end_fill()
time.sleep(50)