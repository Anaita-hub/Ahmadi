#Runtime polymorphism
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()



#len() Example
print(len("Hello"))     # String
print(len([1, 2, 3]))   # List
print(len({1, 2, 3}))   # Set

#compile-Time Style
print(5 + 10)          # Addition
print("Hello" + "Hi")  # String concatenation
print([1] + [2, 3])    # List merge


#magic method
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

v1 = Vector(10)
v2 = Vector(20)

print(v1 + v2)


