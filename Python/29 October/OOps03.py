class Rec:
    def __init__(self,brand,color,speed):
       self.brand   = brand
       self.color = color
       self.speed  = speed 
    def details(self):
        
        print(f"{self.brand}    {self.color}    {self.speed}")

print(f"---Car Details---")
car0=car("Name","Roll NO","      Course")