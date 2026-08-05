from turtle import Turtle,Screen

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("PONG")

paddale=Turtle()
paddale.penup()
paddale.shape("square")
paddale.shapesize(stretch_wid=5,stretch_len=1)
paddale.color("white")
paddale.goto(270,0)

def move_up():
    new_y=paddale.ycor()+20
    paddale.goto(paddale.xcor(),new_y)
def move_down():
    new_y=paddale.ycor()-20
    paddale.goto(paddale.xcor(),new_y)
screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")

game_is_on=True
while game_is_on:
    paddale.forward(10)




screen.exitonclick()