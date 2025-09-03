class Animal:
    def __init__(self,name:str):
        self.name = name
        
    def bark(self):
        pass
    
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")
        
d = Dog("Rex")
print(d.name)
d.bark()