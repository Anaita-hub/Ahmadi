# for variable in iterable
# for with range

#for i in range(start, stop)
for i in range(5,15):
    print(i)

#range
for i in range(8):
    print(i)

#range with step

for i in range(10,0,-4):
    print(i)

#for with list
fruits=["apple","banaba","mango"]
for y in fruits:
    print(y)
    

#for with string:
for ch in "python":
    print(ch)

#for with break
for i in range(10):
    if i ==4:
        break
    print(i)\
#for with continue
for i in range(7):
    if i ==3:
        continue
    print(i)
#for with else
for i in range(3):
    print(i)
else:
    print("loop finished")
#----------------
for i in range(1,11):
    print(i)

for y in "Hello":
    print(y)

colors=["red", "blue","green"]
for c in colors:
    print(c)

num=[3,5,7,2]
total=0
for i in num:
    total+=i
print(total)

a=[1,2,3,4]
for x in a:
    print(x*2)

#Example
sentence="Hello world"
count=0
for x in sentence:
    count +=1
print(count)

#Example
for i in range(10,1,-1):
    print(i)
for i in range(1,11):
    if i ==5:
        break
    print(i)

#Example        
data=[2,4,6,7,8,10]
for x in data:
    if x==7:
        print("found")
    else:
        print("Not found")


#Example
squares=[x*x for x in range (11)]
print(squares)

total=0
for i in range(5):
    num = int(input("Enter Number:"))
    total +=num
print(total)

for var in list:
    for var in list:
        print()
    print()

#Example
for i in range(3):
    for j in range(2):
        print(f"i:{i}, j:{j}")

for i in range(3):
    for j in range(5):
        print(i,j)

for row in range(3):
    for col in range(4):
        print("Row",row,"col",col)

#Example
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()

#Example
data=[["Ali",18],["sara",20],["omid",22]]
for person in data:
    name=person[0]
    age=person[1]
    print(name, "is",age)

#Example
colors=["red","Blue"]
shapes=["circle","square","Traingle"]
for c in colors:
    for s in shapes:
        print(c ,s)

#Example
n=5
for i in range(1,n+1):
    for x in range(i):
        print("*",end=" ")
    print()

#Example
def usd(usd):
    rate=70
    return usd*rate
price = usd(200)
print("afg:" , price)
