from tkinter import *
from tkinter import messagebox

# Function to handle button click
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, END)

# Function to perform the calculation
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the expression
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Initialize the Tkinter window
root = Tk()
root.title("Basic Calculator")

# Entry widget to display the input/output
entry = Entry(root, width=20, font=("Arial", 18), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define button texts
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons and place them on the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = Button(root, relief=SUNKEN,text=text, width=10, height=2, bg="lightgreen", font=("Arial", 14), command=calculate)
    elif text == 'C':
        btn = Button(root, relief=RIDGE,text=text, width=10, height=2, bg="lightcoral", font=("Arial", 14), command=clear_entry)
    else:
        btn = Button(root, text=text, width=10, height=2, font=("Arial", 14),
                        command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()