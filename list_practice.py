"""

list1 = [4, 6, 8, 'a', 'b', [4, 6, 7], 'hello', 1234]

print(list1)
print(type(list1))

print(list1[0])


###################### List slicing ##################

# formula 1 : str[initial position : end position]
# it always skip end position

print(list1[3 : 7])

# Formula 2 : str[:end position]
# it always skip end position
# if initial position is not set, then default initial index is 0.

print(list1[: 4])

# Formula 3 : str[initial position :]
# If end position is not set, then default value is end of the list

print(list1[3: ])

# Formula 4 : str2[initial position :: jump of position]
# default jump position 1
# default initial position is zero '0'

list2 = [4, 6, 8, 'a', 'b', [4, 6, 7], 'hello', 1234]

print(list2[::-1])
print(list2[2::1])


# program : write a python program to print out
# -> square of all the numbers
# -> square of all the number which are divide 3 and 5
# -> find out duplicate values from list.

# -> square of all the numbers
list1 = [5, 6, 8, 30, 5, 15, 6, 5]

for num in list1:
    print(num**2, end=" ")

print("\n")
# -> square of all the number which are divide 3 and 5
for num in list1:
    if num%3 == 0 and num%5 == 0:
        print(num**2, end=" ")

print("\n")
# find out duplicate values from list.
dup  = []
for num in list1:
    var_count = list1.count(num)
    if var_count > 1 and num not in dup:
        print(num)
        dup.append(num)
    else:
        continue
"""

###################################### list methods ##############

print(dir(list))

"""
'append', 'clear', 
'copy', 'count', 
'extend', 'index', 
'insert', 'pop', 
'remove',
'reverse', 'sort'
"""


####### add data to the list #######

"""
list1 = [5, 7, 8, 2]

# append : this method add data to the list at the end position

list1.append(9)
print(list1)

new_list = ['a', 'b', 'c']
list1.append(new_list)

print(list1)

# insert method : This method add data to the list at specific position or index.

list11 = [5, 3, 2, 1, 8]

list11.insert(1, 11)

print(list11)
"""

"""
list11 = [5, 3, 2, 1, 8]
ele_index = list11.index(2)
list11.remove(2)
list11.insert(ele_index, 4)

print(list11)


# extend method : this method can update list with another list data.

lista = [4, 5, 6]
listb = [8, 3, 99, 100]

listb.extend(lista)

print(listb)

############################# Remove data from list ########################

listc = [5, 6, 3, 4, 3]
# remove method : this method any specific value from the list

output = listc.remove(3)
print(output)
print(listc)

# pop method : pop method can remove data specific position/index and return it
#              default index is -1

listd = [5, 6, 3, 4, 3, 11]

# pop without index, default last value will be removed
output1 = listd.pop()
print(output1)

# pop with index
output2 = listd.pop(2)
print(output2)

print(listd)


# Clear Method : clear method remove all the data from the list

liste = [3, 5, 2, 3]

liste.clear()

print(liste)

# Delete the list from memory

listf = [5, 6, 7]

del listf  # it will remove the list from the memory
print(listf)
"""


#######################################################
"""
# reverse method


# option 1
list1 = [4, 2, 6, 1, 8, 9]

list1.reverse()

print(list1)

# option 2

list11 = [4, 2, 6, 1, 8, 9]

result = reversed(list11)

output = []
for i in result:
   output.append(i)
#print(" result :",result)
print("\n")
print("output :", output)
print("list11 : ", list11)

# option 3

list22 = [5, 76, 2, 3, 1, 8]
result2 = list22[::-1]

print("result2 :", result2)
print("list22 :", list22)

# option 4:
list33 = [5, 7, 82, 6, 10]
output33 = []
for i in range(-1, -len(list33)-1, -1):
    output33.append(list33[i])

print("output33 :", output33)
print("list33 :", list33)

"""
#########################################################

# sorting of the list
"""
# sort method
lista = [4, 6, 8, 3, 1]
listb = ['hello', 'haw', 'are', 'you']
lista.sort(reverse=True)
listb.sort()
print("lista :", lista)
print("listb :", listb)

# sorted method
listc = [4, 2, 5, 7, 1]

output = sorted(listc, reverse=True)
for val in output:
    print(val, end=' ')

"""

###############################################
# shallow copy and deep copy

"""
# Shallow Copy
list1 = [6, 4, 8, 2, 1]
list2 = list1

list2.append(9)

print("list1 :", list1)
print("list2 :", list2)

print("_"*20)

# Deep Copy

lista = [4, 2, 6, 8, 1]
listb = lista.copy()

listb.append(56)



print("lista :", lista)
print("listb :", listb)


#################################################
# list comprehention

list1 = [5, 7, 3,  8, 5, 2, 6, 3, 7]
output = []

for i in list1:
    if i%2 == 0:
        continue
    else:
        output.append(i)
print(output)

output2 = [x**2 for x in list1]
print(output2)

output3 = [x for x in list1 if x%2 != 0]
print(output3)

output4 = [(x, list1.count(x)) for x in list1]
print(output4)

output5 = [(x, y) for x in range(3) for y in range(3)]
print(output5)

output6 = [(x, "odd") if x%2 != 0 else (x, "even") for x in list1]
print(output6)


list1 = ['z', '5', '7', '3', '8', 'a', 'bre']

list1.sort()
print(list1)
"""
######################################


list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9]

# 1st, 3rd, 6th
#
# for i in range(len(list1)):
#     if i == 1 or i == 3 or i == 6:
#         list1.pop(i)
#     else:
#         continue
#
# print(list1)

index_list = [1, 3, 6]
output_list = []
for val in list1:
    val_index = list1.index(val)
    if val_index in index_list:
        continue
    else:
        output_list.append(val)

print(output_list)



































