from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()
        self.level=1
        self.goto(-280,250)
        self.update_score()
    def update_score(self):
        self.write(f"Level: {self.level}", align="left",font=FONT)
    def increase_level(self):
        self.clear()
        self.level+=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
        
