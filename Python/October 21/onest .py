
# Accept a string and display it in reverse order. First solve using a loop; then try string slicing.
# Example: Python → nohtyP
# Concepts: Strings, loops, slicing
 
"""text="Good Morning"
Reversed_String=text[::-1]
print(text)
print(f"Reversed text : {Reversed_String}")

text="Good Morning"
i=""
for a in text:
    i = a + i
print(i)
"""

# Check whether a word reads the same forward and backward, ignoring letter case.
# Example: Madam → Palindrome
# Concepts: String methods, slicing, if-else

Input_=input("Enter Your Word :  ")
print("Checking Panlindrome...  ")
print()
Reversed_String=Input_[::-1]
Input_hii= Input_.lower()
Reversed_String_hii = Reversed_String.lower()

if Input_hii ==Reversed_String_hii:
    print("Yes.{Input_} is a Palindrome")
else:
    print("This is not a Palindrome")

