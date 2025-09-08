class Time:
    def init(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __lt__(self,other:class):
        pass        


t1 = Time(10, 30)
t2 = Time(12, 15)

print(t1)      
print(t2)       
print(t1 < t2)  
print(t2 < t1)  