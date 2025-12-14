#self.name is public(default)
#self._age is protected(_)

#self.__salary is private(__)

class Person:
    def __init__(self):
        self.__secret = "Hidden"

p = Person()
# p.__secret ❌
print(p._Person__secret)  # Works (name mangling)


#Getter and Setter Methods
class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age



#Example
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book with {self.pages} pages"

    def __len__(self):
        return self.pages

b = Book(100)
print(b)
print(len(b))

#Real Example
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.balance)
