class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog("Buddy", 3)
print(dog.name)  # Buddy
print(dog.age)   # 3


#Methods in class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "is barking!")

dog = Dog("Rocky")
dog.bark()


#class Attributes
class Dog:
    species = "Canine"  # class attribute

    def __init__(self, name):
        self.name = name

dog1 = Dog("Max")
dog2 = Dog("Leo")

print(dog1.species)
print(dog2.species)



