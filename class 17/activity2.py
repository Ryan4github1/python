import random
options = ["rock","paper","scissor"]
user_choice=input("choose rock, paper or scissor: ")
computer_choice=random.choice(options)
print("you chose:", user_choice)
print("computer chose:", computer_choice)
if user_choice==computer_choice:
    print("it's a tie")
elif user_choice =="rock" and computer_choice=="scissors":
    print("you win")
elif user_choice =="scissors" and computer_choice=="paper":
    print("you win")
elif user_choice =="paper" and computer_choice=="rock":
    print("you win")
else:
    print("you lose")