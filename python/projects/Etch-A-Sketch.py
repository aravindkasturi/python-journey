#More turtle graphics, Event listeners, state and multiple instances
from turtle import Turtle, Screen
himi=Turtle()
screen=Screen()

def move_forward():
    himi.forward(10)
def move_backward():
    himi.backward(10)
def turn_right():
    new_heading=himi.heading()-10
    himi.setheading(new_heading)
def turn_left():
    new_heading=himi.heading()+10
    himi.setheading(new_heading)
def clear():
    himi.clear()
    himi.penup()
    himi.home()
    himi.pendown()
    
def circle():
    himi.circle(60)
    
screen.listen()
screen.onkey(key="w", fun=move_forward)    #onkey is higher-order fun here cuz it is taking other fun as inp
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.onkey(key="space", fun=circle)
screen.exitonclick()
