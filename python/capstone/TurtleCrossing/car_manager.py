from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        rand_chance=random.randint(1,6)
        if rand_chance==1:
            ak=Turtle()
            ak.shape("square")
            ak.shapesize(stretch_wid=1,stretch_len=2)
            ak.color(random.choice(COLORS))
            ak.penup()
            ak.setheading(180)
            new_y=random.randint(-250,250)
            ak.goto(300,new_y)
            self.all_cars.append(ak)

    def move_car(self):
        for i in self.all_cars:
            i.forward(self.car_speed)
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
            
    