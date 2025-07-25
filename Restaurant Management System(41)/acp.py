import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x300")

choices = ["Rock", "Paper", "Scissors"]

user_label = tk.Label(window, text="Your Choice: ", font=("Arial", 14))
user_label.pack(pady=10)

computer_label = tk.Label(window, text="Computer's Choice: ", font=("Arial", 14))
computer_label.pack(pady=10)

result_label = tk.Label(window, text="Result: ", font=("Arial", 16, "bold"))
result_label.pack(pady=20)

def play(user_choice):
    computer_choice = random.choice(choices)
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"
    result_label.config(text=f"Result: {result}")

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

window.mainloop()