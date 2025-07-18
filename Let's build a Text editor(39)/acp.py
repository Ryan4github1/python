from tkinter import *

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    interest = (principal * rate * time) / 100
    result_label.config(text="Simple Interest = " + str(round(interest, 2)))

window = Tk()
window.title("Simple Interest")
window.geometry("300x250")

Label(window, text="Enter Principal").pack()
principal_entry = Entry(window)
principal_entry.pack()

Label(window, text="Enter Rate (%)").pack()
rate_entry = Entry(window)
rate_entry.pack()

Label(window, text="Enter Time (years)").pack()
time_entry = Entry(window)
time_entry.pack()

Button(window, text="Calculate", command=calculate_interest).pack(pady=10)
result_label = Label(window, text="")
result_label.pack()

window.mainloop()