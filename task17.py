class Session:
    def login(self,name:str):
        self.name = name
        print(f"{self.name} logged in")
        
    def logout(self):
        print(f"{self.name} logged out")
        
s = Session()
s.login("Ali")
s.logout()
        