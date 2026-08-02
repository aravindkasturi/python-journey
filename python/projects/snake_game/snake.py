from turtle import  Turtle
POS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
class Snake:
    def __init__(self):
        self.turtle_list=[] 
        self.create_snake()
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
        self.turtle_list[0].forward(MOVE_DIST)







