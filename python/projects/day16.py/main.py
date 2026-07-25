from turtle import Turtle,Screen

himmi=Turtle()       #creating new obj from blueprint
himmi.shape("turtle")  #object attributes
himmi.color("green")
himmi.forward(100)
my_screen=Screen()
print(my_screen.canvwidth)
my_screen.exitonclick()
