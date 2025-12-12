# Type Casting
"""Type casting in Python refers to the process of converting a value from one data 
type to another. This can be useful in various situations, such as when you need
to perform operations between different types or when you need to format data in
a specific way. Also known as data type conversion."""

"""Python has several built-in functions for type casting:
int(): Converts a value to an integer.
float(): Converts a value to a floating-point number.
str(): Converts a value to a string.
list(), tuple(), set(), dict() and bool()"""


"""Type Casting Examples
Basic examples of type casting in python:"""

# Converting String to Integer:
str_num = "26"
int_num = int(str_num)
print(int_num) # Output: 26
print(type(int_num)) # Output: <class 'int'>

# Converting Float to Integer:
float_num = 108.56
int_num = int(float_num)
print(int_num) # Output: 108
print(type(int_num)) # Output: <class 'int'>

# #Types of Typecasting
# There are two types of type casting in python:
#          • Implicit type casting
#          • Explicit type casting

# Implicit Type Casting
""" It is performed automatically by the Python interpreter. This
usually occurs when performing operations between different data types, and
Python implicitly converts one data type to another to avoid data loss or errors."""
# Implicit type casting from integer to float
num_int = 10
num_float = 5.5
result = num_int + num_float # Integer is automatically converted to float
print(result) # Output: 15.5
print(type(result)) # Output: <class 'float'>

#Explicit Type Casting
"""Also known as type conversion, is performed manually by the programmer
using built-in functions. This is done to ensure the desired type conversion and to
avoid unexpected behavior."""

# Converting String to Integer:
str_num = "26"
int_num = int(str_num)
print(int_num) # Output: 26
print(type(int_num)) # Output: <class 'int'>

# Converting a value to boolean:
bool(0) # Output: False
bool(1) # Output: True