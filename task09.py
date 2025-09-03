class Temperature:
    def __init__(self,celsius:float):
        self.celsius = celsius
        
    @property
    def fahrenheit(self):
        return (9 / 5) * self.celsius + 32
    
t =  Temperature(0)
print(t.celsius)
print(t.fahrenheit)