from turtle import  Turtle
POS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.turtle_list=[] 
        self.create_snake()
        self.head=self.turtle_list[0]

    def create_snake(self):
        for turtle in range(3):
            ak=Turtle("square")
            ak.penup()
            ak.color("white")
            ak.goto(POS[turtle])
            self.turtle_list.append(ak)

    def move(self):
        for i in range(len(self.turtle_list)-1,0,-1):
            new_x=self.turtle_list[i-1].xcor()
            new_y=self.turtle_list[i-1].ycor()
            self.turtle_list[i].goto(x=new_x,y=new_y)
        self.head.forward(MOVE_DIST)

    def move_up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


