import random
class FruitQuiz:
    def __init__(self):
        self.fruit={'apple':'red',
                    'orange':'orange',
                    'watermelon':'green',
                    'banana':'yellow'}
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruit.items()))
            print("what is the color of ",fruit)
            user_answer = input()
            if(user_answer.lower()==color):
                print("correct answer")
            else:
                print("WRONG!!!!!!!!!")
            option = int(input("enter 0 to continue : "))
            if (option):
                break
print("welcome to fruit Quiz")
fq = FruitQuiz()
fq.quiz()