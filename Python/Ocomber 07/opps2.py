"""
Define a Student class with attributes name, grade, percentage, and team.
• Include an __init__ method to initialize these attributes.
• Add a method student_details that prints the student’s details in the format:
"<name> is in <grade> grade with <percentage>%, from team <team>".
"""
class  Student_Class:
    def __init__(self,Name,Grade,Percentage,Team):
        self.name = Name 
        self.percentage = Percentage
        self.grade = Grade
       
        self.team = Team
    def Show_Details(self):
        print(f"Name : {self.name}\nGrade : {self.grade}\nPercentage : {self.percentage} \nTeam : {self.team}\n ")


Student1 = Student_Class("Shekhar","A+","99.8%","Blackwood")
Student2 = Student_Class("Aksay","A+","99.8%","Blackwood")
Student3 = Student_Class("Rudra","A+","99.8%","New York")
Student4 = Student_Class("Rishi","A+","99.8%","New York")
Student = Student_Class("Golu","A+","99.8%","London")
Student = Student_Class("Ram","A+","99.8%","Los Angles")
Student = Student_Class("Priyanka","A+","99.8%","Los Angles")
Student = Student_Class("Deva","B+","55.8%","London")


# Student1.Show_Details()
# Student2.Show_Details()


for customer in customers:
    customer.Show_Payment()






