set1 = {4, 5, 7, 4, 2}

print(set1)
"""
-> set is a mutable data type
-> set only store unique data, it does not allow duplicate value
->  It does not follow any indexing
-> we can not add list and dict in a set to avoid a duplicate values
"""


set11 = {(2, 3, 4), 'Hello', 'a', 45, 3.5}
print(set11)

set1 = {5, 6, 7, 8}
set2 = {2, 4, 7, 21}

#set3 = set1 + set2
#print(set3)
#method in sets

print(dir(set))

###############################################
"""
'add', 'clear', 'copy', 'difference', 
'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 
'issuperset', 'pop', 'remove', 'symmetric_difference', 
'symmetric_difference_update', 'union', 'update']
"""

# Add data to set

setp = {4, 6, 3, 2}
setq = {2, 1, 8, 3}

setp.update(setq)
print(setp)

# add sinlge value

set1.add('Python')

print(set1)

# remove data from set

set22 = {5, 6, 7, 8, 'Python'}
set22.remove(8)

print(set22)

# pop data from the set
set23 = {5, 6, 7, 8, 11, 'Python', 'a', 2}
output = set23.pop()

print(output)

# Union of sets : it combine two sets together and return all the unique value, it does not modify existing set
set24 = {5, 3, 7, 2, 8}
set25 = {2, 6, 3, 8, 9}

output24 = set24.union(set25)
print(output24)

# difference between two sets
set26 = {5, 3, 7, 2, 8}
set27 = {2, 6, 3, 8, 9}

output26 = set27.difference(set26)
print(output26)


#  intersection between two sets
set28 = {5, 3, 7, 2, 8}
set29 = {2, 6, 3, 8, 9}

output28 = set28.intersection(set29)
print(output28)

# Is subset

set30 = {5, 3, 7, 2, 8}
set31 = {3, 2, 5, 9}

print(set31.issubset(set30))

# is super set method
print(set30.issuperset(set31))


# difference update : remove all the matching element from target set

set11 = {4, 3, 5, 2, 6, 1, 7, 8}
set22 = {3, 7, 6, 8, 9}

set11.difference_update(set22)

print(set11)
print(set22)

# program : remove duplicate elements from the set

list1 = [4, 6, 8, 3, 8, 2, 8]
output = set(list1)
print(list(output))


