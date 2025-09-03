class Person:
    def __init__(self,name:str,age:int,place:str):
        self.name = name
        self.age = age
        self.work = place
        
    def get_info(self):
        return f"{self.name}, {self.age} years old, works at {self.work}"
    
    
class Employee(Person):
    pass

e = Employee("Hasan",25,"Google")
print(e.get_info())
    
    
