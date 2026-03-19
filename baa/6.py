from turtle import *
tracer(0)
screensize(5000,5000)
left(90)
m = 20
for i in range(2):
    forward(3*m)
    left(90)
    backward(10*m)
    left(90)
up()
backward(10*m)
right(90)
forward(8*m)
left(90)
down()
for i in range(2):
    forward(16*m)
    right(90)
    forward(8*m)
    right(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3)
done()