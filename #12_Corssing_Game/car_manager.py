import random
from turtle import Turtle

COLOR = ["red", "orange", "yellow", "green", "pink", "blue", "purple", "green"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cares = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_care(self):
        random_chance = random.randint(1, 6)
        if random_chance == 2:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cares.append(new_car)

    def move_cars(self):
        for car in self.all_cares:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
