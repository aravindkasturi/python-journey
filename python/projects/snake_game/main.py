from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #Turns turtle animation on/off and set delay for update drawings.
screen.listen()

snake=Snake()
food=Food()
score=ScoreBoard()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1) #delay

    #detect collision with food
    if snake.head.distance(food)<12:
        food.new_food()
        snake.extend()
        score.update_score()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    #detect collision with tail
    for turtle in snake.turtle_list[1:]:
        # if turtle == snake.head:
        #     pass
        if snake.head.distance(turtle)<10:
            game_is_on=False
            exit()
    snake.move()
    




screen.exitonclick()