
class StringTools:
    @staticmethod
    def is_palindrome(text:str):
        text = text.lower()
        palindrome = text[::-1]
        # print(palindrome)
        return text == palindrome
    @classmethod
    def from_sentence(cls,text:str):
        return text.split()
    
print(StringTools.is_palindrome("level"))
st = StringTools.from_sentence("I love python")
print(st)
    
