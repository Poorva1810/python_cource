from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk")
class dog(animal):
    def move(self):
        print("i can bark")
h=human()
h.move()
d=dog()
d.move()                    