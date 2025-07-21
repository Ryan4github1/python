from tkinter import *

def check_password():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please type something", fg="red")
    elif length < 5:
        result_label.config(text="Weak password", fg="red")
    elif length < 8:
        result_label.config(text="Okay password", fg="orange")
    else:
        result_label.config(text="Strong password", fg="green")

window = Tk()
window.title("Password Checker")
window.geometry("300x200")

label = Label(window, text="Type your password:")
label.pack(pady=10)

password_entry = Entry(window, show="*")
password_entry.pack()

check_button = Button(window, text="Check", command=check_password)
check_button.pack(pady=10)

result_label = Label(window, text="")
result_label.pack(pady=10)

window.mainloop()