"""
Define a Student class with attributes name, grade, percentage, and team.
• Include an __init__ method to initialize these attributes.
• Add a method student_details that prints the student’s details in the format:
"<name> is in <grade> grade with <percentage>%, from team <team>".
"""
class  Student_Class:
    def __init__(self,Name,Grade,Percentage,Team):
        self.name = Name
        self.grade = Grade
        self.percentage = Percentage
        self.team = Team
    def Show_Details(self):
        print(f"Name : {self.name}\nGrade : {self.grade}\nPercentage : {self.percentage} \nTeam : {self.team} ")


Student1 = Student_Class("Shekhar","A+","99.8%","Blackwood")
Student2 +


Student1.Show_Details()


        






