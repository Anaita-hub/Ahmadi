my_set=[1,2,3,4,5,1,2,3]
print(my_set)
my_set={}
print(type(my_set))
my_empty_set=set()
print(type(my_empty_set))


number=[1,2,3,4,5,6,6]
set_number=set(number)
print(set_number)

my_Set={1,2,3,4,5,6,7,6,5,4,3}
for item in my_Set:
    print(item)


my_Set.add(10)
print(my_Set)

my_Set.update([12,13,14])
print(my_Set)

my_Set.remove(10)
print(my_Set)

Poppe_item=my_Set.pop()
print(Poppe_item)

my_Set.clear()
print(my_Set)

my={1,2,3,"Ali"}
print(my)

set1={1,2,3}
set2={3,4,5}

print(set1 | set2)
print(set1.union(set2))

print(set1 & set2)
print(set1.intersection(set2))

print(set1-set2)
print(set2.difference(set1))

my_list=list(set1)
print(my_list)
print(type(my_list))