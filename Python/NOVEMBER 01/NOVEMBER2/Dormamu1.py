# Problem 9: Student Marks Validation Using Encapsulation
# Logic: Use a private variable __marks to restrict direct modification.
# Provide a setter with boundary conditions (0-100) to validate data and a getter to retrieve it.
class StudentMarks:
    def __init__(self, name):
        self.name = name
        self.__marks = 0  # Private attribute

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Success: Marks set to {self.__marks} for {self.name}.")
        else:
            print(f"Error: Invalid marks ({marks}). Must be between 0 and 100.")

    def get_marks(self):
        return self.__marks

# Creating an object and testing encapsulation
student2 = StudentMarks("Bob")
student2.set_marks(85)   # Valid
student2.set_marks(105)  # Invalid
student2.set_marks(-10)  # Invalid
print(f"{student2.name}'s verified marks: {student2.get_marks()}")
print("-" * 20)