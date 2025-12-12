# Lists in Python 

# create list 

my_list = [1,2,3]
print(my_list) 

print(type(my_list)) 

my_list2 = [1, 'Madhav', 'Keshav', True, 3.14]
print(my_list2) 
print(type(my_list2)) 

my_list3 = [1,2, [3,4] ,True, [5,6,7] ]
print(my_list3) 
print(type(my_list3))  


# Access list - Indexing 
list1 = [10, 20, 30, 40, 50]
# index: 0   1   2   3   4
# index:-5  -4  -3   -2  -1

# first element
print(list1[0])

# second element
print(list1[1])

# last element
print(list1[-1])

# second last element
print(list1[-2])  


# list - slicing 

list2 = [10, 20, 30, 40, 50, 60, 100]
# index: 0   1   2   3   4   5    6
# index: -7 -6  -5  -4  -3   -2  -1

# slicing syntax 
# list_name[start : stop : step]

# start is inclusive, default is 0
# stop is exclusive, default is -1/last index value 

# first 3 elements 
print(list2[0:3:1])

# elements from index 1 to 4
print(list2[1:5])

# last 3 elements 
print(list2[-3:])

# alternative elements 
print(list2[::2]) #step is 2 

# reverse list 
print(list2[::-1]) #step is -1 


# list modify 

my_list = ['apple', 'banana', 'cherry']

print(my_list)

# replace element at index 1
my_list[1] = "blueberry"
print(my_list)

# add element in list 
my_list.append("Mango")
print(my_list)

# remove element from the list 
my_list.remove("cherry")
print(my_list)


# list methods 

# 1 append
fruits = ["apple", "banana", "orange"]
fruits.append("cherry") 
# fruits.append(108) 
print(fruits)  


#2 extend
fruits = ["apple", "orange"]
more_fruits = ["cherry", "mango"] # another list
fruits.extend(more_fruits)
print(fruits)  


#3 insert
fruits = ["apple", "orange"]
fruits.insert(1, "blueberry")
print(fruits) 


#4 remove
fruits = ["apple", "banana", "orange", "banana"]
fruits.remove("banana")
print(fruits)  


#5 clear
fruits = ["apple", "orange"]
fruits.clear()  # empty list
print(fruits) 


#6 finding index
fruits = ["apple", "banana", "cherry", "banana"]
index = fruits.index("banana")
print(index)  # Output: 1

# finding index - within a range
index = fruits.index("banana", 2)
print(index)  # Output: 3


#7 count elements
fruits = ["apple", "banana", "cherry", "banana"]
count = fruits.count("banana")
print(count)  # Output: 2


#8 Reverse list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  


# 9 sorting list
numbers = [40, 10, 30, 20]
numbers.sort() # default sort asc order
print(numbers) 

# sorting list in descending order
numbers.sort(reverse=True)
print(numbers)  

# Sorting strings in a list
fruits = ["cherry", "apple", "banana", 'blueberry']
fruits.sort() # default by chars asc order
print(fruits) 

# Sorting with a key
fruits.sort(key=len, reverse=True) # sort based on len 
print(fruits) 


# 10 pop with index value
numbers = [10, 20, 30, 40]
popped = numbers.pop(2)
print(popped)    # Output: pop 2nd index value 30
print(numbers)   

# pop with defualt
last = numbers.pop()
print(last)      # Output: pop last value by default 40
print(numbers)   


#11 copying list
fruits = ["apple", "banana", "cherry"]
copy_fruits = fruits.copy() # shallow copy
print(copy_fruits)  

# copying list - Modifying the copy does not affect the original list 
copy_fruits.append("mango")
print(copy_fruits) 
print(fruits)        

# Join Lists  

list1 = [1,2,3]
list2 = ['a', 'b']

# using + operator 
final_list = list1 + list2 
print(final_list)

# using append method 
for x in list2:
    list1.append(x)
print(list1)

# using extend method 
list1.extend(list2)
print(list1)


# List comprehensions 

# syntax: 
# list_name = [expressions for item in iterable if condition] 

# 3 main components of list comprehension 
# expression, for clasue, if condition 

# Create a list of squares
squares = [x**2 for x in range(1,6)]
print(squares)

# filter even numbers 
even_list = [x for x in range(1,20) if x%2 == 0]
print(even_list)

# apply function to each element of a list  
my_list = ['apple', 'mango', 'cherry'] 

my_name = "madhav"
print(my_name)
print(my_name.upper()) 

print(my_list)
# print(my_list.upper()) # wrong way  

uppercase_list = [lst.upper() for lst in my_list]
print(uppercase_list) 

# flatten a nested list using list comp 
nested_list = [[1,2], [3,4], [5,6]] 

result = [item for sublist in nested_list for item in sublist] 
print(result)

# first, [1,2] -> 1,2
# second, [3,4] -> 3,4
# third, [5,6] -> 5,6

def flatten_list(lst):
    return [item for sublist in lst for item in sublist] 

final_list = flatten_list(nested_list)
print(final_list)


# List iterations 

fruits = ['apple', 'mango', 'cherry'] 

# using for loop
for fruit in fruits:
    print(fruit)  

print("length of list", len(fruits))

# while loop
index = 0
while index < len(fruits):
    print(fruits[index]) 
    index += 1 


# list functions examples: 
list1 = [1, 9, 11]

print(len(list1))   # find length of list - total element count
print(min(list1))   # find min value in list
print(max(list1))   # find max value in list
print(sum(list1))   # sum of all list elements 

# Tuples in Python 

my_tuple = (1,2,3)
print(my_tuple)
print(type(my_tuple))

# create tuples
# using parenthesis 
my_tuple = (1,2,3)
print(my_tuple)
print(type(my_tuple))

my_tuple1 = (1, "Madhav", True, 3.15)
print(my_tuple1) 

#2. without parenthesis 
tuple1 = 1,2,3
print(tuple1)
print(type(tuple1)) 

# tuple constructor
tuple2 = tuple((1,5,9)) 
print(type(tuple2))
print(tuple2) 

list1 = [1,2,3]
new_tuple = tuple(list1)
print(new_tuple) 

# create a single element 
a = ("a",)  # comma add
print(type(a)) 

# access tuple - indexing 

fruits = ('apple', 'mango', 'cherry') 

print(fruits[0])

print(fruits[-1]) 

# tuple slicing  
new_tuple = (10, 20, 30, 40, 50)

print(new_tuple[0::3])  

# tuple operations 
# concatenate - join tuples 
tuple1 = (1,2,3)
tuple2 = ('a', 'b')

tuple3 = tuple1 + tuple2
print(tuple3)

# repetitive 
tuple2 = (1,2,3) * 3

print(tuple2) 

# checking a element in a tuple 
tuple22 = (1,2,3)
print(1 in tuple22) 

# tuple iteration 
# for loop 
fruits = ('apple', 'mango', 'cherry') 

for i in fruits:
    print(i) 

# while loop 
i = 0 
while i < len(fruits):
    print(fruits[i])
    i += 1  



# tuple methods 
color = ('blue', 'green', 'orange', 'blue')

# count 
print(color.count('green'))

# index 
print(color.index('blue')) 

# tuple functions 

numbers = (2, 3, 1, 4) 

#len 
print(len(numbers)) 
# sum 
print(sum(numbers)) 
# min, max
print(min(numbers)) 
print(max(numbers)) 

# sort 
a = sorted(numbers) # tuple is now list 
numbers_sorted = tuple(a)
print(numbers_sorted) 

# tuple pack and unpack 

a = "Madhav"
b = 21
c = "Engineer" 

tuple_pack = a,b,c
print(tuple_pack) 

name, age, profession = tuple_pack 
print("Name is", name)
print(age)
print(profession) 


# tuple modification 
tuple_numbers = (10, 20, 30)

# tuple_numbers[0] = 100  # error 

# how to mutate/modify tuple
list_numbers = list(tuple_numbers)
print(list_numbers)  

list_numbers[0] = 100 
print(list_numbers) 

tuple_numbers = tuple(list_numbers)
print(tuple_numbers)

# Sets in Python 

# characteristics of set 
#1. unique values/items 
#2. unordered - no indexing 
#3. mutable- add/remove elements
#4. Immutable elements - replace/modify existing elements 

# create set using curly braces 
my_set = {1,2,3}
print(my_set)
print(type(my_set))

# create set using set constructor 
my_set2 = set([4,5,6]) 
print(my_set2)  

# set operations
#adding elements
numbers = {1,2,3,4} 
numbers.add(100)
print(numbers) 

# removing elements 
#remove 
fruits = {'apple', 'mango', 'banana'}
# fruits.remove('banana') # if element not present show error
print(fruits) 

#discard 
fruits.discard('apple') # doesn't show error
print(fruits)


# Set Methods
#1. union - combine elements from 2 sets 
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
# print(union_set) 

# union alternative 
union_set2 = set1 | set2 
# print(union_set2) 

#2. Intersection - common elements 
set1 = {1,2,3,4}
set2 = {3,4,5}
inter_set = set1.intersection(set2)
# print(inter_set) 

# intersection alternative 
inter_set2 = set1 & set2 
# print(inter_set2) 

#3. Difference - element present in first set only but not in second set 
set1 = {1,2,3,4}
set2 = {3,4,5}
diff_set = set1.difference(set2)
# print(diff_set) 

# Difference alternative 
diff_set2 = set1 - set2 
# print(diff_set2) 

#4. Symmetric Difference - element in either set but not in both 
set1 = {1,2,3,4}
set2 = {3,4,5,6}
sdiff_set = set1.symmetric_difference(set2)
# print(sdiff_set)

# Symm Diff alternative 
sdiff_set2 = set1 ^ set2 
# print(sdiff_set2)


# Set Iterations
# for loop
numbers = {1,2,3,4,5}
for i in numbers:
    print(i)

# while loop - doesn't support 


# Set comprehension 
squares = {x**3 for x in range(1,6)} 
print(squares)

# Dictionary in Python

#syntax: 
# my_dict = {'key1':'value1', 'key2':'value2', ...}

#Methods to create dictionary 
# method-1 create dictionary using curly braces 
cohort = {'course':'Python', 
          'Instructor':'MR', 
          'Level': 'Beginner'} 

print(cohort)
print(type(cohort)) 

# Method-2 using dict() constructor 
person = dict(name= 'Madhav', age=20, grade = 'A')
print(person)
print(type(person)) 

# Method-3 using list of tuples 
person2 = dict([('name', 'Madhav'), ('age', 20), ('city', 'Mathura')])
print(person2)
print(type(person2)) 

# Access dictionary values 
student = {
    1: 'Class-X',
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

print(student)
print(type(student)) 

print(student['name'])
print(student['grade'])


# Dictionary Methods 
student = {
    1: 'Class-X',
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# keys
print(student.keys())

# values
print(student.values())

# items
print(student.items())

# get
print(student['name'])
print(student.get('email', 'Nahi hai')) 


# Add/modify items in dictionary 
student = {
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# add item - assign operator
student['email'] = 'madhav@example.com'
print(student)

# modify/replace item - assign operator
student['grade'] = 'A+'
print(student) 

# remove items
# del to remove item 
del student['grade']
print(student)

# pop method
var1 = student.pop('email')
print(var1)
print(student)


# dictionary iteration 
student = {
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# loop through keys 
for keys in student:
    print(keys)

# loop through values
for value in student:
    print(student[value]) 

# using .values() method
for value in student.values():
    print(value)

# loop through both key-value pair  
for keys,value in student.items():
    print(keys, value) 


# Nested dictionary 

main_student = {

    'student1' : {'name': 'Madhav', 'age': 20},
    'student2' : {'name': 'Keshav', 'age': 25, 'grade': 'A'}
} 

print(main_student)

# access value 
print(main_student['student1'])

print(main_student['student1']['name'])
print(main_student['student2']['grade'])


# Dictionary comprehension 

# syntax 
# new_dict = 
# {key_exp : value_exp for item in iterable if condition}

my_dict = {x:x+x for x in range(1,6)}

print(my_dict) 