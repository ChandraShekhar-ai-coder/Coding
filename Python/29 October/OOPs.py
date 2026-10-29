class Student:
    def __init__(self,name,roll_no,course):
       self.name    = name
       self.roll_no = roll_no
       self.course  = course 
    def details(self):
        print(f"---Student Details---")
        print(f"{self.name}    {self.roll_no}    {self.course}")

Student1=Student("Name","01","Course")
Student1=Student("Shekhar","02","Course")
Student1=Student("Anubhav","03","Course")
Student1=Student("Ravan","Roll No","Course")
Student1=Student("Khumbkaran","Roll No","Course")
Student1.details()




