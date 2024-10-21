COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle


class CarManager:
    def __init__(self):
        self.inital_xcor = 300
        self.move_distance = STARTING_MOVE_DISTANCE
        self.car_list = []

    def car_move(self):
        for car in self.car_list:
            new_x = car.xcor() - self.move_distance
            car.setx(new_x)


    def generate_car(self):
        car = Turtle("square")
        car.shapesize(1,2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(self.inital_xcor, random.randint(-230,230))
        self.car_list.append(car)

    def speed_up(self, round):
        self.move_distance += MOVE_INCREMENT*round
