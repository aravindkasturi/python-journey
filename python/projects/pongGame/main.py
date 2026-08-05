from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle,"w")
screen.onkey(l_paddle,"s")

ball=Ball()
scoreboard=Scoreboard()

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.ycor()==260 or ball.ycor()==-260:
        ball.bounce_y()
    if (ball.xcor()>320 and ball.distance(r_paddle)<50) or ball.xcor()>-320 and (ball.distance(l_paddle)<50):
        ball.bounce_x()
    if ball.xcor()>380:
        scoreboard.l_point()
        ball.reset_pos()
    if ball.xcor()<-380:
        scoreboard.r_point()
        ball.reset_pos()
screen.exitonclick()