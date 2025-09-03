from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius:float):
        self.radius = radius
        
    def area(self,):     
        return 3.14 * (pow(self.radius,2))


class Rectangle(Shape):
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
    
c = Circle(5)
r = Rectangle(4,6)
print(c.area())
print(r.area())