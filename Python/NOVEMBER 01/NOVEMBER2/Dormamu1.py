# Problem 7: Animal Sounds Using Inheritance
# Logic: Parent class Animal has eat(). Child classes Dog and Cat inherit from Animal.
# They define their own sound() method to represent specific behaviors while retaining eat().
class Animal:
    def eat(self):
        print("This animal is eating.")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof! Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

# Creating objects and calling methods
dog = Dog()
print("Dog Actions:")
dog.eat()
dog.sound()

print("\nCat Actions:")
cat = Cat()
cat.eat()
cat.sound()
print("-" * 20)