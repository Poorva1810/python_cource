class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am a cat,my name is  {self.name} and my age is {self.age}")
    def make_sound(self):
        print("cat here")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am a dog, my name is {self.name} and my age is {self.age} ")
    def make_sound(self):
        print("dog here")   
cat1=cat("tom",3)
dog1=dog("tiger",4)
for animal in (cat1,dog1):
    animal.info()
    animal.make_sound()             

