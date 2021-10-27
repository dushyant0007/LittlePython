import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBord

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)  # width, height
screen.title("Pong_Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreBord = ScoreBord()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.speed()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect r paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreBord.l_point()
    # detect l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreBord.r_point()



screen.exitonclick()
