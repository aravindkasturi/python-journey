from turtle import Screen
from snake import Snake
import time
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #Turns turtle animation on/off and set delay for update drawings.

snake=Snake()



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1) #delay

    snake.move()





screen.exitonclick()