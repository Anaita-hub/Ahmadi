def say_hello():
    print("Hello class")
say_hello()

def add(a,b):
    print(a+b)
add(5,7)




def is_even(n):
     if n % 2 ==0:
         print("Even") 
     else:
         print ("Odd")
     
is_even(40)
is_even(85)

def usd_to_afg(usd):
    rate=70
    return usd*rate
price=usd_to_afg(300)
print(" price to Afg:", price)


def valid_phone(num):
    return len(num)==10 and num.isdigit()
phone=input("Enter your number:")
if phone.isdigit() and len(phone)==10:
    print("The number you dield is valid")
else:
    print("The number you dield is invalid")
import math
import random
import exampleList 
sumof=exampleList.add(2,3)
print(sumof)

    