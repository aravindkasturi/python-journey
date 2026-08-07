from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Arial", 20, "normal"))
        
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_score()
    def increase_score(self):
        self.score+=1
        self.update_score()