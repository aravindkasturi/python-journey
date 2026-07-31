# import colorgram

# colors = colorgram.extract("hirstpainting.jpeg", 30)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.g                #to extract rgb of colors in image
#     rgb=(r,g,b)
#     rgb_colors.append(rgb)
# print(rgb_colors)
import turtle
from turtle import Screen
import random

turtle.colormode(255)
himmi=turtle.Turtle()
color_list=[(235, 232, 232), (234, 231, 231), (229, 231, 231), (228, 235, 235), (182, 151, 151), (149, 96, 96), (76, 29, 29), (170, 148, 148), (11, 51, 51), (38, 99, 99), (69, 128, 128), (22, 60, 60), (103, 38, 38), (79, 23, 23), (99, 68, 68), (108, 39, 39), (40, 82, 82), (198, 91, 91), (110, 161, 161), (136, 171, 171), (143, 168, 168), (208, 201, 201), (23, 79, 79), (173, 149, 149), (225, 177, 177), (176, 204, 204), (171, 200, 200), (210, 179, 179), (54, 79, 79), (162, 109, 109)]

himmi.speed("fastest")
himmi.penup()
himmi.setheading(225)
himmi.forward(300)
himmi.setheading(0)
himmi.pendown()
for i in range(10):
    for _ in range(10):
        himmi.dot(20,random.choice(color_list))
        himmi.penup()
        himmi.forward(50)
        himmi.pendown()
    himmi.penup()
    himmi.left(90)
    himmi.forward(50)
    himmi.left(90)
    himmi.forward(500)
    himmi.right(90)
    himmi.right(90)
    himmi.pendown()
himmi.hideturtle()
screen=Screen()
screen.exitonclick()