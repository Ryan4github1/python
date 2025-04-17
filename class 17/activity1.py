import random
playing = True
number = random.randint(10,21)
print("i will generate a number between 10-20 and you will have to guess it one at a time")
print("the game ends when you guess the number")
while playing:
    guess = int(input("give me your best guess: "))
    if number==guess:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("your guess is not right, pls guess again")
