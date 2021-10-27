from turtle import Turtle
import turtle


class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(str(self.l_score), move=False, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(str(self.r_score), move=False, align="center", font=("Arial", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
