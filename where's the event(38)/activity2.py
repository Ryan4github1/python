from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    # messagebox.askyesno("ASKYESNO"," shall i quit?")
    # messagebox.showinfo("information", "submit the project")
    # messagebox.showwarning("Alert", "Virus found")
    messagebox.showerror("Alert", "virus found")
button = Button(root, text="scan for virus", command=msg)
button.place(x=40, y=80)
root.mainloop()