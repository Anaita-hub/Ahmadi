class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()



#Method Overriding
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()


#super() Keyword
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age



#Multiple Inheretence
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
c.show()  # A (Method Resolution Order)