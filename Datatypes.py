#  Numeric Types
A = 42
print(type(A))        

F = 3.14
print(type(F))      

com = 1 + 2j
print(type(com))    

# Sequence Types
S = "Hello"
print(type(S))      

L = [1, 2, 3]
print(type(L))    

T = (1, 2, 3)
print(type(T))      

R = range(5)
print(type(R))      

# Mapping Type
D = {"a": 1, "b": 2}
print(type(D))      

# Set Types
s = {1, 2, 3}
print(type(s))        

FS= frozenset({1, 2, 3})
print(type(FS))  

# Boolean Type
B = True
print(type(B))       

# None Type
N = None
print(type(N))       


# Identifiers rules
# 1. Can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# 2. Cannot start with a digit.
# 3. Cannot contain special characters (e.g., @, #, $, %, etc.).
# 4. Cannot be a reserved keyword (e.g., if, else, for, while, etc.).
# 5. Case-sensitive (e.g., myVar and myvar are different identifiers).
# 6. Should be descriptive and meaningful.

# mutable and im-mutable
# mutable: list, set, dictionary, bytearray
# im-mutable: int, float, complex, string, tuple, frozenset, bytes, range, None, boolean

# properties of list
# square brackets
# mutable
# index based operation - positive and negative indexing
# ordered collection
# allowed duplicate values
# homogeneous and heterogeneous

# tuple
# im-mutable version of list
# round brackets/parenthesis
# index based operation - positive and negative indexing
# ordered collection
# allowed duplicate values
# homogeneous and heterogeneous 

# set
# curly brace
# duplicates not allowed
# unordered collection
# - mutable
# - no indexing, no slicing
# homogeneous and heterogeneous but supports only immutable data types as elements

# Properties of dictionary
# curly brackets with key-value pairs
# mutable
# ordered collection
# keys must be unique and immutable data types
# no indexing 




# type casting
# print(int(34.5)) #34
# print(float(46)) #46.0
# print(str(100)) #'100'
# print(list("Hello")) # ['H', 'e', 'l', 'l', 'o']
# print(list([100]))
# print(tuple([1, 2, 3])) # (1, 2, 3)
# print(set([1, 2, 3, 3, 2, 1])) # {1, 2, 3}
# print(dict(a=1, b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}

# print(float(32+8j)) # TypeError: float() argument must be a string or a real number, not 'complex'

# print(complex(5,45)) # (5+45j)

# print(bool(0)) # False
# print(bool(1)) # True






a = "Application"

print(a.endswith("n"))



# print(a.title())  a-z, A-Z, 0-9
# print(a.isalnum()) # True or False

# print(dir(a)) # 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
