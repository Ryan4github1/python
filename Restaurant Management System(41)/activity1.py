import tkinter as tk
from tkinter import *
def calculate_bill():
    fries_qty = int(fries_entry.get() or 0)
    lunch_qty = int(Lunch_entry.get() or 0)
    cheese_burger_qty = int(cheese_burger_entry.get() or 0)
    drinks_qty = int(drinks_entry.get() or 0)
    total = (fries_qty * 2 + lunch_qty * 2 +cheese_burger_qty *2.5 + drinks_qty * 1)
    bill_window = tk.Toplevel(root)
    bill_window.title("bill details")
    Label(bill_window, text="Bill amount", font=("Arial", 16, "bold")).pack(pady=10)
    bill_details = (
        f"fries meal: {fries_qty} x $2 = ${fries_qty * 2}\n"
        f"lunch meal: {lunch_qty} x $2 = ${lunch_qty * 2}\n"
        f"cheese_burger meal: {cheese_burger_qty} x $2.5 = ${cheese_burger_qty * 2.5}\n"
        f"drinks meal: {drinks_qty} x $1 = ${drinks_qty}\n"
        f"\nTotal: ${total:.2f}"
    )
    Label(bill_window, text=bill_details, font=("Arial", 12), justify="left").pack(pady=10)
    Button(bill_window, text="close",command=bill_window.destroy).pack(pady=10)
root=Tk()
root.title("restaurant management App")
root.geometry("400x400")
header_Label = tk.Label(root, text="bob's restaurant", font=("Arial", 16, "bold"))
header_Label.pack(pady=10)
frame= Frame(root)
frame.pack(pady=10)
Label(frame, text="fries meal ($2):").grid(row=0,column=0, pady=5, sticky="w")
fries_entry = Entry(frame)
fries_entry.grid(row=0, column=1, pady=5)
Label(frame, text="Lunch meal ($2):").grid(row=1,column=0, pady=5, sticky="w")
Lunch_entry = Entry(frame)
Lunch_entry.grid(row=1, column=1, pady=5)
Label(frame, text="cheese_burger meal ($2.5):").grid(row=2,column=0, pady=5, sticky="w")
cheese_burger_entry = Entry(frame)
cheese_burger_entry.grid(row=2, column=1, pady=5)
Label(frame, text="Drinks ($1):").grid(row=3,column=0, pady=5, sticky="w")
drinks_entry = Entry(frame)
drinks_entry.grid(row=3, column=1, pady=5)
place_order_button=tk.Button(root, text="Place order",command=calculate_bill)
place_order_button.pack(pady=20)
root.mainloop()
