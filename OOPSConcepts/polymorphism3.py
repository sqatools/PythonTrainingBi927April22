"""
Operator Overloading : one operation performing different task with different type of data
"""

# Plus operator
num1 = 40
num2 = 50
#print(num1+num2)
print(num2.__add__(num1))
print(dir(int))

str1 = "Hello"
str2 = "Good Morning"
#print(str1 + str2)

print(str1.__add__(str2))
print(dir(str))

