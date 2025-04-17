import random
options = ["pizza", "burger", "sushi"]
user_choice = input("Choose pizza, burger, or sushi: ").lower()
computer_choice = random.choice(options)
print("You chose:", user_choice)
print("Computer chose:", computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "pizza" and computer_choice == "burger":
    print("You win!")
elif user_choice == "burger" and computer_choice == "sushi":
    print("You win!")
elif user_choice == "sushi" and computer_choice == "pizza":
    print("You win!")
else:
    print("You lose")