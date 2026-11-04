with open(r"message.txt", "r", encoding="utf-8") as file

print(file.read())
file.close()

with open("students.txt", "r", encoding="utf-8") as file:
    print(file.read())
