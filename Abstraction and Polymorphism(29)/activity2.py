from abc import ABC, abstractmethod
class Animals(ABC):
    def move(self):
        pass
class Human(Animals):
    def move(self):
        print("i walk and run")
class snake(Animals):
    def move(self):
        print("i can crawl")
R=Human()
R.move()
K=snake()
K.move()