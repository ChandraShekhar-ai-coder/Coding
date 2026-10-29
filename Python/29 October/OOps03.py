class Rectangle:
    def __init__(self,length,breath):
       self.length   = length
       self.breath = breath
       
    def details(self):
        
        print(f"{self.length}    {self.breath} {self.length}   ")

print(f"---Rectangle Details---")
Rectangle0=Rectangle(10,24)