class car:
    def __init__(self,length,breath,speed):
       self.length   = length
       self.breath = breath
       self.speed  = speed 
    def details(self):
        
        print(f"{self.length}    {self.breath}    {self.speed}")

print(f"---Car Details---")
car0=car("Name","Roll NO","      Course")