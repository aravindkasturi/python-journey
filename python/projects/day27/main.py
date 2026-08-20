from tkinter import *

def button_clicked(): 

    s=input.get()

    my_label.config(text=s)

window =Tk()
window.title("GUI")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#label
my_label=Label(text="AK68", font=("Arial",24,"italic"))
my_label.grid(column=0,row=0) #to show on screen

#button
button1=Button(text="Click here", command=button_clicked)
button2=Button(text="Click here", command=button_clicked)
button1.grid(column=1,row=1) 
button2.grid(column=2,row=0)
#Entry 
input =Entry()
input.grid(column=3,row=2)


window.mainloop()