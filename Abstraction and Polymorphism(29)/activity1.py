from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("passed value: ", x)
        @abstractmethod
        def task(self):
            print("we are in Absclass task")
class test_class(Absclass):
    def task(self):
        print("we are in test_class task")
test_obj= test_class()
test_obj.task()
test_obj.print(100)
# obj=Absclass()
# obj.task()