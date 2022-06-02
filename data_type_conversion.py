"""
-> int
-> float
-> string
-> list
-> tuple
-> dict
-> set
-> Boolean
"""

################# Int #####################

# int to float
"""
num1 = 10
print(type(num1))
num3 = float(num1)
print(type(num3))
"""
# int -> list # can not convert into list
"""
num2 = 30

new = list(num2)
print(new)
"""

# int -> string
"""
num = 30
print(type(num))
print(num)
new = str(num)
print(type(new))
print(new)
"""

# int -> tuple : can not convert int into tuple
"""
num = 30
print(type(num))
print(num)
new = tuple(num)
print(new)
"""

# int -> dict : can not convert int into dict.
"""
num = 30
print(type(num))
print(num)
new = dict(num)
print(new)

#TypeError: 'int' object is not iterable
"""

# int -> set # can not convert int into set
"""
num = 30
print(type(num))
print(num)

new = set(num)
print(new)
"""
# int -> boolean : can not convert int into boolean

########################### Float ######################
# Float -> int
"""
num = 30.25
print(type(num))
print(num)

new = int(num)
print(new)
print(type(new))
"""
# Float -> string
"""
num = 30.25
print(type(num))
print(num)

new = str(num)
print(new)
print(type(new))
print(new[3])
"""
# Float -> list : can not convert float into list
# Float -> tuple : can not convert float into tuple
# Float -> dict : can not covert float into dict
# Float -> set : can not convert float into set
# Float -> Boolean : can not convert float into boolean.

############################ String ######################

# string -> int


"""
# Word can no convert into int
str1 = "Hello"
print(type(str1))

new = int(str1)
print(new)
"""
"""
# The string which has only numbers can convert into int
str2 = "3456"
new_num = int(str2)
print(type(new_num))
print(new_num)
"""


# string -> float

"""
str1 = "Hello"
print(str1)
print(type(str1))

new_float = float(str1)
print(new_float)
"""
"""
# The string which has only numbers can convert into float
str2 ="5678"

new_float2 = float(str2)
print(new_float2)
print(type(new_float2))

"""

# String -> list
"""
str1 = "Hello"
print(str1)
print(type(str1))

new_list = list(str1)
print(new_list)
print(type(new_list))

print(new_list[3])

"""

# string -> tuple
"""
str1 = "Hello"
print(str1)
print(type(str1))

new_tuple = tuple(str1)
print(new_tuple)
print(type(new_tuple))
"""
# string -> dictionary
"""
str1 = "Hello"
print(str1)
print(type(str1))

new_dict = dict(str1)
print(new_dict)
"""

# we can convert string dictionary into dictionary with json module
"""
import json

str2 = '{"name" : "rohit", "age" : 25, "mobile": 23436565}'
print(str2)
print(type(str2))
print(str2[0])

output = json.loads(str2)

print(output)
print(type(output))

print(output['mobile'])
"""

# String -> sets
"""
str1 = "Hello Good"
print(str1)
print(type(str1))
set1 = set(str1)
print(set1)
print(type(set1))
"""
# String to Boolean :

# If string has any value then it will True else if string is empty then it will return false
"""
str1 = "H"
print(str1)
print(type(str1))

new = bool(str1)
print(new)

"""

############################### List #####################

# list -> int # can not convert list into int
"""
list1 = [4, 6, 7]
new = int(list1)
print(new)
"""
# list -> float : can not convert list into float
# list -> string

"""
list1 = [4, 6, 7]

new = str(list1)
print(new)
print(type(new))
print(new[0])
"""

# list -> tuple
"""
list1 = [5, 6, 7]
new = tuple(list1)

print(new)
print(type(new))
"""
# list -> dict : can not convert list into dict, dict does not follow indexing
"""
list1 = [6, 8, 90]

new = dict(list1)
print(new)
"""

# list -> set
"""
list1 = [5, 7, 8, 3, 2, 3, 5]

new = set(list1)

print(new)
print(type(new))

# list -> Boolean
"""
"""
#list1 = [5, 7, 8]   # True
list1 = []  # False
print(bool(list1))
"""
############################# Tuple #############################

#-> tuple -> int # can not convert tuple into int
# tuple -> float : can not convert tuple into float
# tuple -> string
"""
tuple1 = (5, 7, 8)

new = str(tuple1)
print(new)
print(type(new))

"""
# tuple ->  list
"""
tuple1 = (5, 7, 8)
new = list(tuple1)
print(new)
print(type(new))
"""
# tuple -> dict : can not convert tuple to dict
# tuple -> set
"""
tuple1 = (5, 76, 2, 3, 8, 5, 2)
new = set(tuple1)
print(new)
print(type(new))
"""
# tuple -> boolen
"""
#tuple1 = (2, 5, 80) # True
tuple1 = () # False
print(bool(tuple1))

"""
################################# Dictionary #########################

# dict -> int : can not convert dict into int
# dict -> float  : can not convert dict into float
# dict -> string

dict1  = {'a': 123, 'b' : 345}
new = str(dict1)
print(new)
print(type(new))

# dict -> list : can not convert dict to list
# dict -> tuple : can not convert dict into tuple
# dict -> set : can not convert dict into set
# dict -> bool : same as tuple, list and string

######################### Set ########################

# set -> int : can not convert set into int
"""
set1 = {4, 6, 8}
new = int(set1)
print(new)
"""

# set -> float : can not convert set into float
#set -> string
"""
set1 = {4, 6, 8}
new = str(set1)
print(new)
print(type(new))
"""
# Set -> list
"""
set1 = {5, 7, 8, 3, 6, 2, 5}

new = list(set1)
print(new)
print(type(new))
"""
# Set -> tuple

"""
set1 = {5, 7, 2, 6, 2}
new = tuple(set1)
print(new)
print(type(new))
"""

# set -> dict : can not convert set into dict

set1 =  {5, 4, 6, 7}

new = dict(set1)
print(new)

# set -> Boolean : will follow same property like string, list tuple etc.




