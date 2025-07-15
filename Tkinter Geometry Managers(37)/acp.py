import tkinter as tk
from datetime import datetime
from tkinter import messagebox

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = datetime(year, month, day)
        today = datetime.now()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for day, month, and year.")

window = tk.Tk()
window.title("Age Calculator")
window.geometry("300x300")

tk.Label(window, text="Enter your Date of Birth", font=("Arial", 14)).pack(pady=10)

tk.Label(window, text="Day:").pack()
day_entry = tk.Entry(window)
day_entry.pack()

tk.Label(window, text="Month:").pack()
month_entry = tk.Entry(window)
month_entry.pack()

tk.Label(window, text="Year:").pack()
year_entry = tk.Entry(window)
year_entry.pack()

tk.Button(window, text="Calculate Age", command=calculate_age).pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

window.mainloop()