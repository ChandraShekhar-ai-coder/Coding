with open("message.txt","r",encoding="utf-8") as file:
    print(file.read())
with open("message.txt", "a", encoding="utf-8") as file:
    print(file.write("/hii golu"))