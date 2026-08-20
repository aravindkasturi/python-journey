from tkinter import *

def button_clicked():
    miles=entry.get()
    km=float(miles)*1.6
    label3.config(text=(km))

window=Tk()
window.minsize(width=500,height=300)
window.title("Mile to Km converter")
window.config(padx=200,pady=200)

label1=Label(text="is equal to")
label1.grid(column=0,row=1)

entry=Entry()
entry.grid(column=1,row=0)

label2=Label(text="Miles")
label2.grid(column=2,row=0)

label3=Label(text="")
label3.grid(row=1,column=1)

label4=Label(text="Km")
label4.grid(row=1,column=2)

button=Button(text="Calculate",command=button_clicked)
button.grid(row=3,column=1)
window.mainloop()