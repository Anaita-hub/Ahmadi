from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10

class Circle(Shape):
    def area(self):
        return 20

shapes = [Rectangle(), Circle()]

for shape in shapes:
    print(shape.area())


#Example2

class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def lift_off(entity):
    entity.fly()

lift_off(Bird())
lift_off(Airplane())
