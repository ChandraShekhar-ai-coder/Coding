class car:
    def __init__(self,brand,color,speed):
       self.brand   = brand
       self.color = color
       self.speed  = speed 
    def details(self):
        
        print(f"{self.brand}    {self.color}    {self.speed}")

print(f"---Car Details---")
car0=car("Name","Roll NO","      Course")
car1=car("Mclau","01    ","      LLB")
car2=car("   Shekhar","02  ","   MBA")
car3=car("   Anubhav","03  ","   MCA")
car4=car(" Ravan","04    ","     B.Tech")
car5=car("  Khumbkaran","05   ","BCA")
car0.details()
car1.details()
car2.details()
car3.details()
car4.details()
car5.details()