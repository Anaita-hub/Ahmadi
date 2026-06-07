# ============================================================
# Advanced Lesson 1: Decorators
# Instructor: Anaita Ahmadi | GEO Organization
# ============================================================

import time
import functools

# --- What is a Decorator? ---
# A decorator is a function that wraps another function
# to add extra behavior without changing its code.

# --- Basic Decorator ---
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(">> Before the function runs")
        result = func(*args, **kwargs)
        print(">> After the function runs")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Fatima")

# --- Practical Decorator: Timer ---
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def calculate_sum(n):
    return sum(range(n))

print("Sum:", calculate_sum(1000000))

# --- Practical Decorator: Logger ---
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] '{func.__name__}' returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(5, 3)

# --- Decorator with Arguments ---
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Welcome, {name}!")

greet("Zahra")

# --- Property Decorator ---
class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self._grade = value
        else:
            raise ValueError("Grade must be between 0 and 100")

    @staticmethod
    def school_name():
        return "GEO Academy"

    @classmethod
    def create_top_student(cls):
        return cls("Top Student", 100)

s = Student("Maryam", 85)
print(f"Student: {s._name}, Grade: {s.grade}")
s.grade = 90
print(f"Updated Grade: {s.grade}")
print("School:", Student.school_name())

top = Student.create_top_student()
print(f"Top student: {top._name}, Grade: {top.grade}")

# ============================================================
# Practice Exercise:
# 1. Write a decorator that checks if a user is logged in
#    before running a function
# 2. Write a decorator that catches and prints any exceptions
# 3. Use @property to create a Circle class with a radius
#    property that auto-calculates area
# ============================================================
