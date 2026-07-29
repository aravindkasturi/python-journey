from turtle import Turtle, Screen
import random

himmi=Turtle()

himmi.shape("turtle")
himmi.color("Green")

# sqaure
# for _ in range(4):
#     himmi.forward(100)
#     himmi.right(90)

#dashed line
# for _ in range(15):
#     himmi.forward(10)
#     himmi.penup()  #no drawing
#     himmi.forward(10)
#     himmi.pendown() #on paper

#pentagon
# for _ in range(5):
#     himmi.forward(100)
#     himmi.right(72)   #360//5sides=72

colors=["lime green","green yellow", "pale green", "wheat","yellow",
        "red","navajo white","dark goldenrod","dark green","orange red"]

def draw_shape(num_sides):
    angle=360//num_sides
    for _ in range(num_sides):
        himmi.forward(50)
        himmi.right(angle)

for shape_side_n in range(3,10):
    himmi.color(random.choice(colors))
    draw_shape(shape_side_n)










screen=Screen()
screen.exitonclick()  #this wont disappear window unless click

