from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=500,height=400)
# user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)


color=["red","green","yellow","blue"]

for i in range(0,4):
    red=Turtle(shape="turtle")
    red.color(color[i])
    red.penup()
    red.goto(x=-240,y=-50+(i*50))


screen.exitonclick()