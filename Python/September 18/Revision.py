"""
# Question:
# 

print("Write a Python program to manage the marks of 10 students.\n1. Create a list called marks containing marks of 10 students.")
students_List = [77,88,55,96,54,5,5,54,4,84]
print()

print(" 2. Use a for loop to check the marks of every student.")
print()

print(" 3.For each student If marks are 90 or above, print Grade A \nIf marks are 75–89, print Grade \n If marks are 60–74, print Grade C \n If marks are 40 59, print Grade D\n If marks are below 40, print Fail")
print()



for sm in students_List:
    print(f"Marks Of Students : {sm}")
    if sm>=90:
        print("Grade A")
    elif sm >75:
        print("Grade B")
    elif sm >60:
        print("Grade C")
    elif sm >40:
        print("Grade D")    
    else:
        print("Congratulations You Are failed")



print("4. Also calculate and print:\n Total marks \n Average marks\n Number of students who passed\n Number of students who failed \n Highest marks\n Lowest marks")

students_List = [77,88,55,96,54,5,5,54,4,84]
print("Total marks :")
print(sum(students_List))
print("Maximum Value : ")
print(max(students_List))
print("Minimum value : ")
print(min(students_List))
print("Average marks : ")
print(sum(students_List)/len(students_List))

# 5. At the end, print the complete result in a clear format.
# Example input:
# marks = [95, 82, 67, 45, 32, 76, 88, 59, 91, 38]
# Expected output format:
# Student 1: 95 - Grade A
# Student 2: 82 - Grade B
# Student 3: 67 - Grade C
# Total Marks: ...
# Average Marks: ...
# Passed Students: ...
# Failed Students: ...
# Highest Marks: ...
# Lowest Marks: ...

print("---Result Analysis---")
print("Student's Marks : ",students_List)

marks = [c]

total = 0
passed = 0
failed = 0

for i in range(len(marks)):
    mark = marks[i]
    total = total + mark

    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "Fail"

    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    print("Student", i + 1, ":", mark, "-", grade)

average = total / len(marks)

print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Passed Students:", passed)
print("Failed Students:", failed)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# Q1. List
# Create a list of 10 numbers and print:
# The first element
# The last element
# The first 5 elements using slicing
# The last 
my_list=[95, 82, 67, 45, 32, 76, 88, 59, 91, 38]
print(my_list[0])
print(my_list[-1])
print(my_list[-5:])
print(my_list[-3:])


#Q2. List + Loop
#Create a list of 10 numbers. Use a for loop to print only the even numbers.
myy_list=[95, 82, 67, 45, 32, 76, 88, 59, 91, 38]
for i in myy_list:
    if i%2==0:
        print(i)

"""

# Q3. List + Conditional Statements
# Create a list of marks:

marks = [45, 78, 32, 90, 67, 25, 88]
index = 0
for index, score in enumerate(marks):
    student_num = index + 1 
    if score >= 40:
        print(f"Student {student_num}: {score}, Passed")
    else:
        print(f"Student {student_num}: {score}, Failed")
    
#Create a tuple containing 7 numbers. Use a loop to calculate and print the sum of all numbers.
marks = (45, 78, 32, 90, 67, 25, 88)
i = 0
for i in marks:
    i= i +1
    print(sum(i))
















