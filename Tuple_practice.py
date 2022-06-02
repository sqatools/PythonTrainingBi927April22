tuple1 = (4, 6, 7, 3, 'Hello', 3.5)

print(type(tuple1))
print(tuple1)

# positive index
print(tuple1[1])

# Negative Index
print(tuple1[-2])

# Slicing ion tuple
print(tuple1[1:4])

# Method for the tuple

print(dir(tuple))
"""
'count', 'index'
"""

tup1 = (5, 7, 8, 3, 7, 2, 11, 3)
print("count of 3:", tup1.count(3), tup1.index(11))

###################################################
"""
for var in tup1:
    print(var%2 == 0, var)
"""
tupa = (5, 6, 7)
tupb = (7, 8, 9)

tupc = tupa + tupb
print(tupc)

###################
# Write a program to get all value from the tuple and their factorial
# .e.g factorial : 5 = 5*4*3*2*1
#output = [(val, fat)....]

input_tuple = (3, 5, 7, 2, 8)
output = []

for val in input_tuple:
    print(val)
    fact = 1
    for i in range(1, val+1):
        fact = fact * i

    output.append((val, fact))


print(output)


input_tuple = (3, 55, 7, 2, 8, 11, 1)

print("Max value :", max(input_tuple))
print("Min value :", min(input_tuple))
print("Sum of numbers :", sum(input_tuple))




