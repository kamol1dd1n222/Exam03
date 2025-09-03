class Author:
    def __init__(self,author:str):
        self.author = author
        
    
class Book:
    def __init__(self,title:str,ega:str):
        self.title = title
        self.ega = ega    
        
    def get_info(self):
        return f"Book: {self.title}, Author: {self.ega}"
    
a = Author("Alisher Navoiy").author
b = Book("Xamsa", a)
print(b.get_info())
    
    