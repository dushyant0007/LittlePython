import random
import turtle as t
# instead of using timmy = turtle.Turtle()
#    now we can do timmy = t.Turtle()
import random

from turtle import Turtle
# instead of using timmy = turtle.Turtle()
#    now we can do timmy = Turtle()

import turtle as t
# instead of using timmy = turtle.Turtle()
#    now we can do timmy = t.Turtle()

from turtle import Turtle
# instead of using timmy = turtle.Turtle()
#    now we can do timmy = Turtle()

from turtle import *

# this import everything from turtle package
# Not a good practices

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.speed(-10)  # 0 - fastest ,  10 for slowest

timmy.penup()
timmy.right(90)
timmy.forward(300)
timmy.pendown()
timmy.left(90)

colorList = ['MediumOrchid', 'DarkSalmon', 'Black', 'Pink', 'RoyalBlue', 'DodgerBlue', 'gold']

for i in range(3, 100, 1):
    turnAngle = 360 / i
    for j in range(i):
        timmy.color(random.choice(colorList))
        timmy.forward(50)
        timmy.left(turnAngle)

my_screen = t.Screen()

my_screen.exitonclick()
