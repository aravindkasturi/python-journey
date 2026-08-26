from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]

    numbers = [
        '0','1','2','3','4','5','6','7','8','9'
    ]

    symbols = [
        '!','@','#','$','%','^','&','*','(',')',
        '_','+','-','=','[',']','{','}','|','\\',
        ';',':',"'",'"',',','.','<','>','/','?',
        '`','~'
    ]

    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_num=random.randint(2,4)
    password=""
    for char in range(nr_letters):
        random_choice = random.choice(letters)
        password+=random_choice
    for char in range(nr_symbols):
        random_choice = random.choice(symbols)
        password+=random_choice
    for char in range(nr_num):
        random_choice = random.choice(numbers)
        password+=random_choice
    entry3.delete(0,END)
    entry3.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data={
        website:{
        "email":email,
        "password":password
        }
    }
    if len(password)==0 or len(website)==0:
        messagebox.showinfo(title="Empty", message="Fields can't be empty")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered:  \nEmail: {email}\nPassword: {password}")
        if is_ok:
            with open("data.json","r") as data:
                s=json.load(data) # reads data
            with open("data.json","w") as data:
                s.update(new_data) #update data
                json.dump(s,data,indent=4) #write data
                entry1.delete(0,END)
                entry3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

label1=Label(text="Website: ")
label1.grid(row=1,column=0)
entry1=Entry(width=35)
entry1.grid(row=1,column=1,columnspan=2)
entry1.focus()

label2=Label(text="Email/Username: ")
label2.grid(row=2,column=0)
entry2=Entry(width=35)
entry2.grid(row=2,column=1,columnspan=2)
entry2.insert(0,"aravind@email.com")

label3=Label(text="Password: ")
label3.grid(row=3,column=0)
entry3=Entry(width=23)
entry3.grid(row=3,column=1)

button1=Button(text="Generate Passoword",command=generate_pass)
button1.grid(row=3,column=2)

button2=Button(width=36,text="Add",command=save)
button2.grid(row=4,column=1,columnspan=2)

window.mainloop()