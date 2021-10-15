import random

import colorgram
import turtle as t

colors = colorgram.extract('img.jpg', 10)
# this going to return Color objects, which let you
# access rgb,hsl, ans what proportion of the image was that color.
first_color = colors[0]
print(f"first_color = {first_color}")
print(f"colors = {colors}")

rgb_colorList = []
for i in range(0, 10):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    new_color = (r, g, b)
    rgb_colorList.append(new_color)

t.colormode(255)
# t.colormode allow us to make change in colors and pass in rgb form


# colorList = [(204, 159, 102), (130, 79, 118), (84, 91, 135), (231, 217, 195), (200, 138, 162), (218, 221, 231),
#              (231, 220, 226), (134, 151, 189), (222, 203, 133), (141, 91, 71)]


timmy = t.Turtle()
timmy.penup()
timmy.left(180)
timmy.forward(300)
timmy.left(90)
timmy.forward(200)
timmy.left(90)
timmy.pendown()

for i in range(0, 10):

    for j in range(0, 10):
        timmy.pendown()
        timmy.color(random.choice(rgb_colorList))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)

    if (i + 1) % 2 == 0:
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)
        timmy.forward(50)

    else:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(50)

my_screen = t.Screen()
my_screen.exitonclick()
