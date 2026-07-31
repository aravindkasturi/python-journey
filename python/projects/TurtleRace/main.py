from turtle import Turtle,Screen
import random

is_race_on=False

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

color=["red","green","yellow","blue"]
all_turtles=[]

for i in range(0,4):
    red=Turtle(shape="turtle")
    red.color(color[i])
    red.penup()
    red.goto(x=-240,y=-50+(i*50))
    all_turtles.append(red)

if user_bet:
    is_race_on=True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            wininng_color=turtle.pencolor()
            if wininng_color==user_bet:
                print(f"You won! The {wininng_color} turtle won")
            else:
                print(f"You lost! The {wininng_color} won")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()