class Student:
    def __init__(self,name,roll_no,course):
       self.name    = name
       self.roll_no = roll_no
       self.course  =  course 
    def Details(self):
        print(f"---Student Details---")
        print(f"{self.name}")
    
