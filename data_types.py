print("We are learning python")

"""
Python Data Types:

1. Numbers
      -> Integer
      -> Float
      
      
2. Sequence:
      -> List
      -> String
      -> Tuple
      
3. Dictionary

4. Sets

5. Boolean 
"""

# Integer :
"""
var1 = 345
-> int data type is immutable data type.
-> int data type, there is no limit of data

"""
"""
var1 = 4567
print(type(var1))
var2 = 567893556645654645
print(var2)
print(type(var1))

#

a = 4
b = 5
c = 3

output = a*2+b**2+c**3-50
# 8 + 25 + 27 - 50
# 8 + 52 - 50
# 10
print(output)
print(type(output))
"""

################## FLoat ##################

"""
-> float data type is immutable data type.
-> float data type, there is no limit of data
"""
"""
var3 = 50.5
print(type(var3))
x = 5.4
y = 3.8
z = 3.2
result = (x+y)*5 +  z**3 +  100
print(result)
print(type(result))
"""
########################## String #####################

"""
str3 = ""
str4 = """"""
str1 = "Hello"
print(str1)
print(type(str1))
"""
"""
-> String follows positive and negative indexing.
-> String is immutable data type
-> there is not limit for string data type
"""
"""
#  0 1 2 3 4
#  H E L L O
# -5-4-3-2-1

print(str1[0]) # to read data from string, list, tuple we have to use square bracket with index value
#print(str1(0)) : round bracket is not allowed with indexing
print(str1[-5])

# var1 = -30
# print(type(var1))

str2 = "Hello we are learning python Programming"

# len method : this method helps to get length of given string
# len()
print(len(str2))

print(str2[7])


#len()
"""
str5 = """good"""
# str6 = '''morning'''
# str7 = 'Python'
# str8 = "Program"
#
# print(type(str5), type(str6), type(str7), type(str8))

############################# List ########################
"""
list1 = []
print(type(list1))
#        0  1     2     3      4
list2 = [3, 2.5, 'a', 'Hello', [3, 5]]
#        -5 -4    -3    -2     -1

output = list2[3]
print(output)
print(type(output))
print(output[2])
"""
"""
-> list is mutable data type
-> list follows positive and negative index
-> list can contain any type of data e.g int, float, str, list, tuple, dict, set.
"""
######################### tuple ##################

"""
tuple1 = ()
print(type(tuple1))

#         0  1      2       3       4          5
tuple2 = (5, 'a', 'Python', 30.23, [4, 6, 7], {'a': 123, 'b': 567})
#        -6  -5   -4       -3      -2          -1
print(tuple2)

print(tuple2[2][1])
var1 = tuple2[2]
print(var1[1])
#
# print(tuple2[-2][1])
#
# print(tuple2[5])

# immutable : data can not modify once it is defined
# mutable : we can modify the data
"""
"""
-> tuple follows same indexing like list, string.
-> tuple is immutable data type
-> tuple can contains any type of  data .e.g int, float, string, list
"""

# list1 = [3, 5, 7]
# print(dir(list1))
# list1.append(4)
# print(list1)
#
# tuple1 = (4, 6, 2)
# print(dir(tuple1))
#
# tuple1.index()

################################# Dict data type #######################
        #key : value
dict1 = {'a': 456, 'b': 345}
print(dict1)

print(type(dict1))
"""
-> dict does not follow any index
-> dict is mutable data type
-> only immutable data type can key in the dictionary. e.g int, string, tuple
-> dict does not contains duplicate key, key should be unique.
-> any type of data can be store as value in the dictionary, int, float, list, string , tuple, dict.
"""
"""
dict2 = {'a' : 123, (3, 4, 5) : 45.6, 'Hello': [3, 4, 5], 5: 'Python'}

print(dict2['Hello'])

dict3 = {'a': 345, 'b' : 456, 'c' : 123}

print(dict3['a'])

dict3['d'] = 567

print(dict3)
"""
############################### Sets #################
"""
set1 = set()

print(set1)
print(type(set1))

set2 = {4, 5, (4, 5),  2, 7, 8, 2, 'a'}

print(set2)
"""
"""
-> Set is mutable data type, we can modify it.
-> Set only store unique data, duplicate values is not allowed.
-> Set does not follow any indexing.
-> Set is unstructure data type.
"""

######################### Boolean ######################
# Boolean data type deals in True and False

num1 = 20
num2 = 20

print(num1 == num2)




"""
number : int, float
word, char, para : string
want to store different data with sequence and update it : list
want to store different data and fix data : tuple
store data in random form with unique key: dict
store unique data : set
play with conditional statement : boolean 
"""

num2 = 11

if num2%2 == 0:
    print(True)
else:
    print(False)











