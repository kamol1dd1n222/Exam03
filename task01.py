class Car:
    def __init__(self,brand:str,model:str,year:int):
        self.brand = brand
        self.model = model
        self.year = year
        
    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"
    
car = Car("BMW","M8 Compitation",2025) 
print(car.get_info())       
        