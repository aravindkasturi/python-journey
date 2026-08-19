
from tkinter import *


window =Tk()

window.title("GUI")

window.minsize(width=500,height=300)

#label

my_label=Label(text="AK68", font=("Arial",24,"italic"))

my_label.pack() #to show on screen

def button_clicked(): 

    s=input.get()

    my_label.config(text=s)

#button

button=Button(text="Click here", command=button_clicked)

button.pack() 


#Entry 
input =Entry()

input.insert(END, string="Type")

input.pack()

#text 
text=Text(width=30, height=5)

text.insert(END, "Type")

text.pack()

#spinbox

spinbox =Spinbox(from_=0, to =10, width=4)

spinbox.pack() 

#scale 

scale=Scale(from_=0,to=10)
scale.pack()

#checkbutton

checked_state =IntVar()

checkbutton=Checkbutton(text="Is ON?", variable=checked_state)

checkbutton.pack()



#radiobutton

radio_state=IntVar()

radiobutton1=Radiobutton(text="yes", value=1, variable= radio_state)

radiobutton2=Radiobutton(text="no", value =2, variable =radio_state)

radiobutton1.pack()

radiobutton2.pack()

#Listbox

def list_box(event):

    print(listbox.get(listbox.curselection()))

listbox =Listbox(height=2)

fruits=["Apple", "Orange"]

for i in fruits:
    listbox.insert(fruits.index(i),i)

listbox.bind("<<ListboxSelect>>", list_box)


listbox.pack()

window.mainloop()



