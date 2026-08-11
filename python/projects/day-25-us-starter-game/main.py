import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data=pd.read_csv("50_states.csv")
state_list=data["state"].to_list()
correct_ans=[]
while True:
    answer=turtle.textinput(
        title=f"{len(correct_ans)}/50 correct states",
        prompt="Guess another state"
    ).title()
    if answer=="Exit":
        # with open("missing_states.csv","w") as data:
        #         for i in state_list:
        #             if i not in correct_ans:
        #                 data.write(f"{i} \n")
        missing_states_list=[n for n in state_list if n not in correct_ans]
        missing=pd.DataFrame(missing_states_list)
        missing.to_csv("missing_states")
        exit()
    if answer in state_list:
        correct_ans.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        store_data=data[data.state == answer]
        t.goto(store_data.x.item(),store_data.y.item())
        t.write(answer)        


