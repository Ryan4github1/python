from tkinter import *

def convert():
    try:
        cm = float(entry.get())
        choice = variable.get()
        if choice == "Millimeters":
            result = cm * 10
            unit = "mm"
        elif choice == "Meters":
            result = cm / 100
            unit = "m"
        elif choice == "Kilometers":
            result = cm / 100000
            unit = "km"
        else:
            result_label.config(text="Select a unit.")
            return
        result_label.config(text=f"{result:.4f} {unit}")
    except ValueError:
        result_label.config(text="Enter a valid number.")

window = Tk()
window.title("CM Converter")
window.geometry("300x200")

Label(window, text="Enter length in cm:").pack(pady=5)
entry = Entry(window)
entry.pack()

variable = StringVar(window)
variable.set("Select Unit")
options = OptionMenu(window, variable, "Millimeters", "Meters", "Kilometers")
options.pack(pady=5)

Button(window, text="Convert", command=convert).pack(pady=5)
result_label = Label(window, text="")
result_label.pack()

window.mainloop()