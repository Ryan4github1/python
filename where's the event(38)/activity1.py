from tkinter import*
window = Tk()
window.title("event handler")
window.geometry('300x300')
def handle_Keypress(event):
    """print the character associated to the key pressed"""
    print(event.char)
window.bind("<Key>", handle_Keypress)
def handle_click(event):
    print("\nThe button was clicked!")
button = Button(text="click me!")
button.pack()
button.bind("<Button-3>",handle_click)
window.mainloop()
