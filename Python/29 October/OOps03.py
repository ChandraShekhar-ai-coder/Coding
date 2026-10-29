class car:
    def __init__(self,length,color,speed):
       self.length   = length
       self.color = color
       self.speed  = speed 
    def details(self):
        
        print(f"{self.length}    {self.color}    {self.speed}")

print(f"---Car Details---")
car0=car("Name","Roll NO","      Course")