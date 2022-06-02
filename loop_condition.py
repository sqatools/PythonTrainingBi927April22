# print(1)
# print(2)

# range(initial position, end position, difference between each step)

"""
for i in range(0, 10, 1):
     print(i)
"""

# with 2 step movement

"""
for i in range(0, 10, 2):
    print(i)
"""
# if initial value is not set then default initial value is zero '0'
# if difference of each step is not set, then default value is One '1'
# In loop structure with range , it always skip the last value
'''
for i in range(1, 11):
    print(i)
'''

# print table of any number

"""
num1 = 3

for i in range(1, 11):
    print(i, "*", num1, ":", i*num1)
    
"""
"""
# print all values in single row, we can use end parameter with print
for i in range(10):
    print(i, end='-')

"""

# Apply loop with string

str1 = "GoodMorning"

# for var in str1:
#     print(var, end='')

"""
str_len = len(str1)
print(str_len)

for i in range(1, str_len, 2):
    #print(i)
    print(str1[i], end='')

"""

"""
# Apply loop with list

list1 = [5, 7, 8, 9, 4]

for var in list1:
    print(var, end=" ")

print("\n")

for i in range(len(list1)):
    print(list1[i], end=' ')
"""
"""
# Apply loop with tuple

tuple1 = (5, 7, 8, 3, 4)
for var in tuple1:
    print(var, end=' ')

print("\n")

for i in range(len(tuple1)):
    print(tuple1[i], end=' ')

print("\n")
print(tuple1[0])
"""
# apply loop with dict

"""
dict1 = {'a' : 123, 'b': 456, 'c' : 345}

for var in dict1.items():
    print(var)

"""

"""
dict1 = {'a' : 123, 'b': 456, 'c' : 345}

for key, value in dict1.items():
    #print(key, value)
    if key != 'a':
        print(value)

"""


####################################################
# Get all even number from 1 to 50

"""
for i in range(1, 50):
    if i%2 == 0:
        print(i)

"""

# Get square of all even number and cube of all odd number from 1 to 20.
"""
for i in range(1, 20):
    if i%2 == 0:
        print(i, i**2)
    else:
        print(i, i**3)

"""

########################## Nested Loop Condition #######################
# Address
"""
for i in range(1, 6):
    # Package
    for j in range(1, 4):
        #print('Address:', i, "package:", j)
        print('i :', i, "j :", j)

    print("##"*10)

"""
"""
# provide third place only one vlue
for i in range(1, 6):
    # Package
    for j in range(1, 4):
        #print('Address:', i, "package:", j)
        if i == 3:
            print('i :', i, "j :", j)
            break
        else:
            print('i :', i, "j :", j)

    print("##"*10)
"""

##################################################
"""
parking_list = ['full', 'full', 'full', 'full', 'empty', 'full']

for parking in parking_list:
    #print(parking)
    if parking == 'empty':
        print("we can park our car at parking number :", parking_list.index(parking))
        break
    else:
        continue
"""


############################### use of break and continue #####################

"""
# continue statement
for i in range(10):
    #print(i)
    if i == 3:
        continue
    print("We are going in loop", i)

# break statement
for i in range(10):
    #print(i)
    if i == 3:
        break
    print("We are going in loop", i)
"""

"""
#
for i in range(10):
    #print(i)
    if i <= 3:
        continue
    print("We are going in loop", i)
"""









































