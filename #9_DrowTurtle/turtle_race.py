import random
import turtle
from turtle import Turtle, Screen, penup

is_race_on = True
screen = Screen()
screen.setup(500, 400)
colors = ['red', 'green', 'pink', 'black', 'brown', 'purple']
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color")
all_Turtle = []

y = -40
for turtle_index in range(0, 6):
    tim = Turtle('turtle')
    tim.penup()
    tim.goto(-235, y)
    y = y + 30
    tim.color(colors[turtle_index])
    all_Turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_Turtle:
        if turtle.xcor()>250:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print("Your bet turtle Won!")
            else:
                print("You loose")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
