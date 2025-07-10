from tkinter import *
from datetime import date
window=Tk()
window.title("My first GUI")
window.geometry('500x600')
lbl=Label(text="Enter your name")
lbl.pack()
e=Entry()
e.pack()
def fun():
    name=e.get()
    txt.insert(END,"todays date is:")
    txt.insert(END,date.today())
    txt.insert(END," welcome"+ name)
btn=Button(text="click", comman=fun)
btn.pack()
txt=Text(height=3)
txt.pack()
window.mainloop()