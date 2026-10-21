
# Accept a string and display it in reverse order. First solve using a loop; then try string slicing.
# Example: Python → nohtyP
# Concepts: Strings, loops, slicing
# 
 """text="Good Morning"
Reversed_String=text[::-1]
print(text)
print(f"Reversed text : {Reversed_String}")
"""
text="Good Morning"
i=""
for a in text:
    i = a + i
print(i)