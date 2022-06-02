
"""
str1 = "Hello good morning"

print(str1)
print(type(str1))

str2 = 'Python' \
       'Language'
str3 = "Programming" \
       "is good"
"""
str4 = '''
Hello we are learning
python programming to
improve the skils
'''
str5 = """
Hello we are learning
python programming to
improve the skils


"""

# print(str2)
# print(str3)
# print(str4)
#
# print(str5)


############################ String Formatting ###########
"""
name = 'Ketan'
age = 25
email = 'ketan@gmail.com'

# concantenation of strings
result = "Hello my name is "+name+" and age is "+str(age)+ ", and personal email is "+email
print(result)

# format method
result2 = "Hello my name is {} and age is {}, and personal email is {}".format(name, age, email)
print(result2)

# f string
result3 = f"Hello my name is {name} and age is {age}, and personal email is {email}"
print(result3)

# raw string
new_string = r"Its IPL time \n we are enjoying matches"
print(new_string)

new_string2 = r"Its IPL time \n \t \twe Today's are enjoying matches"
print(new_string2)

"""

##################### Slicing ###################
"""
str1 = "Good Morning"

# Print first two char of string
# formula 1 : str[initial position : end position]
# it always skip end position

print(str1[0: 2])

print(str1[3: 7])

print("negative index output :", str1[2: -2])

# Formula 2 : str[:end position]
# it always skip end position
# if initial position is not set, then default initial index is 0.

print(str1[:7])

new_output = str1[:-3]
print("new output :", new_output)

# Formula 3 : str[initial position :]
# If end position is not set, then default value is end of the string

output = str1[3:]
print("output :", output)


output2 = str1[-3:]
print("output :", output2)


str2 = "Python Programming"

# Formula 4 : str2[initial position :: jump of position]
# default jump position 1
# default initial position is zero '0'

output = str2[::3]

print(output)

# in case of negative index, initial position is -1
output2 = str2[::-1]
print(output2)

# gnimmargorP nohtyP

output2 = str2[::-2]
print(output2)

# gimroPnhy
"""

################################### String Methods ################

str1 = "Python Programming"

print(dir(str1))

"""
'capitalize', 'casefold', 'center', 'count', 
'encode', 'endswith', 'expandtabs', 'find', 
'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 
'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 
'removeprefix', 'removesuffix', 'replace', 
'rfind', 'rindex', 'rjust', 'rpartition', 
'rsplit', 'rstrip', 'split', 'splitlines', 
'startswith', 'strip', 
'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
"""
Mostly used method:

1. count
2. find
3. format
4. index
5. islower
6. isnumeric
7. join
8. lower
9. upper
10. strip
11. split
12. replace
13. Title
14. Swapecase
"""

# 1. count : we can get count of any character in the string
"""
str1 = "Python Programming language"

output = str1.count('P')
print(output)

temp_str = ''
for char in str1:
    if char not in temp_str:
        print(f"char : {char}, count :{str1.count(char)}")
        temp_str = temp_str + char
    else:
        continue

"""


# 2. find : using this method we can search char, substring and word in given string
#           it returns the index of required substring if exist, else it will return -1
#           if it is not available in the string.
"""
str1 = "Python Programming language"

output = str1.find('Pro')
print(output)

output2 = str1.find('languages')
print(output2)

print(str1.index("languages"))

"""


# 3. format : format method provides way to add variable in the string.
"""
name = 'Pratik'
age = 25
print("Hello my name is {} and my age is {}".format(name, age))
print(f"Hello my name is {name} and my age is {age}")

"""

# 4. index : index method position of given substring/word/char in the target string.
#            it shows error if substring/word/char is not there in the target string.

"""
str1 = "Python Programming language"

output = str1.index("Pro")
print(output)  # 7

output2 = str1.index("languages")
print(output2)  # it will throw error string not found
"""

"""
str2 = "Hello"

print(str2[4])
print(str2.index('o'))
"""

# 5. islower

"""
str1 = "PythoM PrograMming LanguagE"

word = 'Word'
print(word.islower())

# Write a program to convert all upper case to lower case and lower case and to upper case
# program1 : get count of all the upper cases char and lower case character.
# program2 : get count of vowels from each word.
# program3 : covert all vowels to upper case and consonant to lower case.
#           vowels = "aeiou"

temp_str = ''

for char in str1:
    #print(char)
    if char.islower():
        temp_str = temp_str + char.upper()
    elif char.isupper():
        temp_str = temp_str + char.lower()
    else:
        temp_str = temp_str + char

print(temp_str)
"""

# 6. isnumeric : this method check given string has only number or not, It return True
#                if string contains only numbers else return False if contains Alphabates
"""
str1 = "345678A"

result = str1.isnumeric()
print(result)

str2 = ""
result2 = str2.isalnum()
print(result2)
"""
"""
# Program : find out all the numeric string from target string
str1 = "Python234 Programming 4567 language is bes4444t 45667899990 learn 45667899590"

word_list = str1.split(" ")
print(word_list)

for word in word_list:
    #print(word)
    if word.isnumeric():
        print(word)
    else:
        continue
"""

# program : write a python program to get all the mobile numbers from given string.


input_str = """
Python's 2347234562 convenience has made 55 it 
the 22 most 34 popular 4567234562 language for 
machine learning and artificial intelligence. 
Python's 66 flexibility 4527254562 has allowed 
Anyscale to make ML/AI scalable 
from  4563434562 laptops to clusters.
"""
"""
Steps to follow:
step1 : get word_list from target string using split() method.
step2 : go through each word in the word_list using loop
step3 : check each word is numeric and its len should be 10 with if condition.
step4 : if condition is matching the print word else continue
"""

# step1 : get word_list from target string using split() method.
word_list = input_str.split(" ")
# step2 : go through each word in the word_list using loop
for word in word_list:
    # step3 : check each word is numeric and its len should be 10 with if condition.
    if word.isnumeric() and len(word) == 10:
        # step4 : if condition is matching the print word else continue
        print(word)
    else:
        continue




# 7. join  : we can join string with any delimeter or char.

"""
str1 = "Python"
word_list = ['Hello', 'How', 'are', 'you']

result = "#".join(str1)
print(result)

result2 = " ".join(word_list)
print(result2)
"""
"""
str1 = "Hello"
str2 = "Good morning"

output= str1 +" "+ str2
print(output)

print("{} {}".format(str1, str2))
print(f"{str1} {str2}")
"""

# 8. lower : convert upper character to lower
"""
str1 = "HELLO"
str1.upper()
"""

# 9. upper : Convert lower character to upper
"""
str1 = "hello"
str1.upper()
"""

# 10. strip : this method trim spaces from left and right side of the string.
"""
str1 = "  Python Program Language  "

print(str1)

result = str1.strip()
print(result)

# Remove left side space

result_l = str1.lstrip()
print(result_l)

# Remove right side space

result_right = str1.rstrip()
print(result_right)

"""

# 11. split : This  method split entire string list o words parts as the delimeter apply
"""
str1 = "Python,Programming,language"
str2 = "Python Programming language"

output = str1.split(",")
print(output)

output2 = str2.split(" ")
print(output2)
"""

# 12. replace : This method replace one word from another from given string.

"""
str2 = "Hello we are leaning JAVA language"
output = str2.replace("JAVA", "Python")
print(output)
"""
# Program4 : write a python to replace following words in the given string:
# Java -> Python
# Programming -> Learning
# is -> Are

input_str = """
Python's 2347234562 convenience is Programming made 55 it 
the 22 most 34 popular 4567234562 language for 
machine is learning and JAVA artificial intelligence. 
Python's 66 Programming flexibility 4527254562 has allowed 
Anyscale to make ML/AI  Programming scalable 
from  4563434562 laptops is clusters.
"""

# 13. Title :

str1 ="its langauge class"

output = str1.title()
print(output)

# 14. Swapecase

str1 ="Its lanGauge ClAss"

output2 = str1.swapcase()
print(output2)

"""
# Program : write a python to count each char from string without using count method.

str1 = "Its new day, we are learning"

count_dict = {}

for char in str1:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print(count_dict)

"""
# program : Write a python to print given output from input string.
str1 = "MONTUEWEDTHUFRISATSUN"
output = ['SUN', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON']

b1 = 0
b2 = 3
output = ""
for i in range(len(str1)):
    if b2 <= len(str1):
        output = output +" "+ str1[b1:b2]
        b1 = b1 + 3
        b2 = b2 + 3
    else:
        break

print(output)

result = output.strip().split(" ")
result.reverse()
print(result)

























































