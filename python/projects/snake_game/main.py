from turtle import Screen, Turtle
import time
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #Turns turtle animation on/off and set delay for update drawings.
pos=[(0,0),(-20,0),(-40,0)]
ak=Turtle()
turtle_list=[]
for turtle in range(3):
    ak=Turtle("square")
    ak.penup()
    ak.color("white")
    ak.goto(pos[turtle])
    turtle_list.append(ak)
    # ak.pendown()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)   #delay
    for i in range(len(turtle_list)-1,0,-1):
        new_x=turtle_list[i-1].xcor()
        new_y=turtle_list[i-1].ycor()
        turtle_list[i].goto(x=new_x,y=new_y)
    turtle_list[0].forward(20)
    turtle_list[0].left(90)

        



# screen.onkey(key="w",fun=move_forward)




screen.exitonclick()