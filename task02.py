class Student:
    def __init__(self,name:str,age:int,grade:int):
        self.name = name
        self.age = age
        self.grade = grade
        
    def introduce(self):
        if self.grade == 1:
            return f"My name is {self.name}, I am {self.age} years old, studying in {self.grade}st course."
        elif  self.grade == 2:
            return f"My name is {self.name}, I am {self.age} years old, studying in {self.grade}nd course."
        elif self.grade == 3:
            return f"My name is {self.name}, I am {self.age} years old, studying in {self.grade}rd course."
        else:
            return f"My name is {self.name}, I am {self.age} years old, studying in {self.grade}th course."
            
s = Student("Kamoliddin",19,1)
print(s.introduce())