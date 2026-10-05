"""
#Q1. Set Operations — 5 Marks

# Create two sets:

# A = {10, 20, 30, 40, 50}
# B = {30, 40, 50, 60, 70}

# Write a Python program to display:

# 1. Union


# 2. Intersection


# 3. Difference of A and B


# 4. Difference of B and A


A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}
a=A.union(B)
b=A.intersection(B)
c=A.difference(B)
d=A.symmetric_difference(B)
print(a)
print(b)
print(c)
print(d)



# Q2. Dictionary + Loop — 5 Marks

# Create a dictionary containing 5 students and their marks.

# Example:

# students = {
#     "Rahul": 85,
#     "Aman": 72,
#     "Priya": 91,
#     "Neha": 67,
#     "Rohan": 78
# }

# Using a for loop:

# Display each student's name and marks.

# Display only those students who scored 80 or above.

students = {
    "Rahul": 85,
    "Aman": 72,
    "Priya": 91,
    "Neha": 67,
    "Rohan": 78
}


for name, marks    in students.items():
 print(f"{name} : {marks}")

print("\nstudents who scored 80 or above.")
for name, marks    in students.items():
 if marks>80:

  print(f"{name} : {marks}")




# Q3. Reverse a Number — 5 Marks

# Write a Python program to input a number and print its reverse.

# Example:

# Input: 12345
# Output: 54321

# Condition: Use a while loop.
# Do not convert the number into a string.

num=int(input("Enter your No."))

    # Q4. Conditional Statements — 5 Marks

    # Write a Python program to input a student's marks and display the grade:

    # Marks	Grade

    # 90–100	A+
    # 80–89	A
    # 70–79	B
    # 60–69	C
    # 50–59	D
    # Below 50	Fail


    # Also handle invalid marks such as greater than 100 or less than 0.

marks=int(input("Your marks  "))
print(f"Your Marks: {marks}")

if marks <0 or marks>100:
    print("invalid marks")
elif marks>=90:
    print("Grade A+")
elif marks>= 80:
    print("Grade A")
elif marks>= 70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>= 50:
    print("Grade D ")
else:
    print("Failed ")
"""


# Q5. Dictionary + Conditional + Loop — 10 Marks ⭐

# Create a dictionary containing 5 students and their marks.

# Write a program that uses a loop and conditional statements to display:

# Student name

# Marks

# Grade

# Pass/Fail
students = {
    "Rahul": 85,
    "Aman": 72,
    "Priya": 91,
    "Neha": 67,
    "Rohan": 78
}


for name, marks    in students.items():
    if marks <0 or marks>100:
        print("invalid marks")
    elif marks>=90:
         grade="Grade A+"
        status = "Pass"
    elif marks>= 80:
        grade="Grade A"
        print("Pass")
    elif marks>= 70:
        grade="Grade B"
        print("Pass")
    elif marks>=60:
        grade="Grade C"
        print("Pass")
    elif marks>= 50:
         grade="Grade D ")
        print("Pass")
    else:
        grade="Failed "
        
print(f"{name} : {marks}")



















































