from turtle import Screen
from snake import Snake
import time
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #Turns turtle animation on/off and set delay for update drawings.
screen.listen()

snake=Snake()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1) #delay

    snake.move()





screen.exitonclick()