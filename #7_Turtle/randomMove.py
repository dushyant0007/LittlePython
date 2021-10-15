import turtle as t
# instead of using timmy = turtle.Turtle()
#    now we can do timmy = t.Turtle()
from random import randint
import random

from turtle import Turtle
# instead of using timmy = turtle.Turtle()
#    now we can do timmy = Turtle()

from turtle import *

# this import everything from turtle package
# Not a good practices

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.speed(0)
timmy.pensize(5)

angle = [0, 90, 180, 270]

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for i in range(100):
    timmy.left(random.choice(angle))
    timmy.forward(30)
    timmy.color(random_color())

my_screen = t.Screen()
my_screen.exitonclick()
