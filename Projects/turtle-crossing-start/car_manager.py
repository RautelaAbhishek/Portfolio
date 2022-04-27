import time
from turtle import Turtle
from random import randint, randrange,choice 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_change = randint(1,6)
        if random_change == 1: 
            new_car  = Turtle("square")
            new_car.penup()
            new_car.resizemode('user')
            new_car.shapesize(1,2)
            new_car.color(choice(COLORS))
            random_y = randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)


    def move_across(self):
        for car in self.all_cars:
            car.back(self.move_speed)
    
    def level_up(self):
        self.move_speed += MOVE_INCREMENT