#dict1 = {'key', 'value'}

"""
-> dict store the data in key value format
-> dict only contain unique key, duplicate key is not allowed.
-> only immutable data type can be key in the dictionary
-> dict is mutable data type
-> dict can contain any type of data as value.
"""
dict1 = {'a' : 123, 'b' : 567, 'c' : 234}

# Add data to dictionary
dict1['e'] = 456
print(dict1)

# add duplicate key in the dict
dict1['a'] = 999
print(dict1)

#########################################################################

dict2 = {1 : [4, 5, 6], 'a' : (4, 5, 7), 2.3 : {'name' : 'Ram'}, ('p', 'q', 'r') : 'Python'}

# Get all the keys
print(dict2.keys())

# Get all the values
print(dict2.values())

# Get name from the dictionary
name = dict2[2.3]
print(name['name'])

print(dict2[2.3]['name'])

print(dict2[('p', 'q', 'r')][0])

"""
school = {

    'student' : [
                  {'name' : 'stud1', 'email': 'stud1@gmail.com', 'mobile' : 42234},
                  {'name' : 'stud2', 'email': 'stud2@gmail.com', 'mobile' : 454234},
                  {'name' : 'stud3', 'email': 'stud3@gmail.com', 'mobile' : 451234},
                  {'name' : 'stud4', 'email': 'stud4@gmail.com', 'mobile' : 456234},
                  {'name' : 'stud5', 'email': 'stud5@gmail.com', 'mobile' : 463543234},
                 ],
     'teachers' : [
                    {'name' : 'teach1', 'email': 'teach1@gmail.com', 'mobile' : 42256543},
                    {'name' : 'teach2', 'email': 'teach2@gmail.com', 'mobile' : 42256543},
                    {'name' : 'teach3', 'email': 'teach3@gmail.com', 'mobile' : 42445433},
                    {'name' : 'teach4', 'email': 'teach4@gmail.com', 'mobile' : 422333654},
                    {'name' : 'teach5', 'email': 'teach5@gmail.com', 'mobile' : 422533654},
                ]

}

# get stud5 mobile number from given data

student_name = 'stud3'
student_details = school['student']
print(student_details)

for data in student_details:
    #print(data['name'])
    if data['name'] == student_name:
        print(data['mobile'], data['email'])
    else:
        continue

# Get email of student3
# Get mobile number of teach5
# Get student name who mobile is 451234

teacher_details = school['teachers']

for details in teacher_details:
    print(details)
    if details['name'] == 'teach5':
        print(details['mobile'])

stud_mobile = 456234
for detail in student_details:
    if detail['mobile'] == stud_mobile:
        print(detail['name'])

print(school['student'][3]['name'])

dict1 = {'a' : 345, 'b' : 234, 'c' : 56}

for var in dict1.items():
    print(var)


for key, val in dict1.items():
    print(key, val)
"""
########################### Dict Methods ####################

print(dir(dict))
"""
'clear', 'copy', 'fromkeys', 
'get', 'items', 'keys', 
'pop', 'popitem', 
'setdefault', 
'update', 'values']
"""

"""
# Remove data from the dict

# pop method : in this method we have to mention key name, which is going to be removed.
dict11 = {'a' : 345, 'b' : 234, 'c' : 56}

output = dict11.pop('c')
print(output)

print(dict11)

# pop item

output2 = dict11.popitem()
print(output2)

print("key :", output2[0], "value:", output2[1])
print(dict11)

# program: move data from one dict to another dict

dict22 = {'d' : 567, 'a' : 345, 'b' : 234, 'c' : 56, 'aa' : 'Python', 123: 'program', 'f' : 567}

dict22['g'] = 777
print(dict22)

output3 = dict22.popitem()
print(output3)

# program: move data from one dict to another dict

dict22 = {'d' : 567, 'a' : 345, 'b' : 234, 'c' : 56, 'aa' : 'Python', 123: 'program', 'f' : 567}
dict33 = {}
temp = dict22.copy()

for key, val in temp.items():
    output = dict22.pop(key)
    dict33[key] = output


print("dict22 :", dict22)
print("dict33 :", dict33)


############### Get all keys #########

print(dict33.keys())
print(dict33.values())


dict44 = {'d': 567, 'a': 345, 'b': 234, 'c': 56, 'aa': 'Python', 123: 'program', 'f': [567, 54]}

dict55 = {'e' : 333, 'f' : 234}

dict44.update(dict55)

print("dict44", dict44)

############################# Program ##################
# Program:  write a python program to print this output
str1 = "Python is Good Language"
dict1 = {'P': 'PythoN', 'i' : 'IS', 'G': 'GooD', 'L': 'LanguagE'}

"""

dictp = {}
for i in range(20):
    dict1.setdefault(f'a{i}', '30')

print(dictp)

dict44 = {'d': 567, 'a': 345, 'b': 234, 'c': 56, 'aa': 'Python', 123: 'program', 'f': [567, 54]}
new = 'r'

output = dict44.setdefault('b12', 40)
output1 = dict44.setdefault('b13', 50)
output3 = dict44.setdefault('f1', 500)


print(output)
print(output1)
print(output3)

dictp = {'a1': 500}
for i in range(5):
    print(dictp.setdefault(f'a{i}', 50))

print(dictp)
print(dict44)

# for key, value in dict44.items():
#     output = dict44.setdefault(new, '40')
#     print(output)



dictq = {'d': 567, 'a': 345, 'b': 234, 'c': 56, 'aa': 'Python', 123: 'program', 'f': [567, 54], 'b12': 40, 'b13': 50, 'f1': 500}


dictq['f'] = [567, 500]
print(dictq)

###########################################
keys = ('a', 'b', 'c')
val = 40

new_dict = dict.fromkeys(keys, val)
print(new_dict)

new_dict2 = dict.fromkeys(keys)
print(new_dict2)














