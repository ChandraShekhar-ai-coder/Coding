class Car:
    def __init__(self,brand,color,speed):
       self.brand   = brand
       self.color = color
       self.speed  = speed 
    def details(self):
        
        print(f"{self.roll_no}    {self.name}    {self.course}")

print(f"---Student Details---")
Student0=Student("Name","Roll NO","      Course")
Student1=Student(" Name","01    ","      LLB")
Student2=Student("   Shekhar","02  ","   MBA")
Student3=Student("   Anubhav","03  ","   MCA")
Student4=Student(" Ravan","04    ","     B.Tech")
Student5=Student("  Khumbkaran","05   ","BCA")
Student0.details()
Student1.details()
Student2.details()
Student3.details()
Student4.details()
Student5.details()