import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
def calculator_denominations():
    try:
        amount = int(entry_amount.get())
        denominations = [100, 50, 20, 10, 5]
        result_text = ""
        if amount <= 0:
            messagebox.showerror("Error","please enter a positive amount.")
            return
        for i in denominations:
            count = amount // i
            if count > 0:
                result_text += f"{i} x {count} = {i * count}\n"
            amount %= i
        result_label.config(text= result_text)
    except ValueError:
        messagebox.showerror("Error","please enter a valid number.")
root = tk.Tk()
root.title("Denomination calculator")
root.configure(bg= "#b2c0ce")
root.geometry('350x300')
font_style= ("Helvetica", 30)
label = ttk.Label(root, text="Enter Amount:", font=font_style)
label.grid(row=0, column=0, padx=10, pady=10)
entry_amount = ttk.Entry(root, font=font_style, width=20)
entry_amount.grid(row=0,column=1,padx=10,pady=10)
calculate_button = ttk.Button(root, text="calculate", command=calculator_denominations)
calculate_button.grid(row=1,column=0,pady=10)
result_label = tk.Label(root, text="", justify="left", anchor="w", bg='#e6f2ff', font=("helvetica", 20))
result_label.grid(row =2, column= 0, padx=10, pady=10, sticky="w")
root.mainloop()