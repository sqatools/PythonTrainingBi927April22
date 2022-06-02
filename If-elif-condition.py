"""
if <condition>:
    code

if <condition>:
    code
else:
   code

"""
"""
num = 11

if num%2 == 0:
    print("This is even number")
else:
    print("This is not even number")
"""
"""
Logical operator

== : equal to operator
> : greater than operator
< : less than operator
>= : greater that equal to.
<= : less than equal to
!= : not equal to.

and operator
or operator
"""

# Input method to read user input
# input() : by default value enter as string
"""
user_input = int(input("Please enter your number :"))

if user_input%2 == 0:
    print("This is even number")
else:
    print("This is odd number")
"""

"""
while True:
    user_input = int(input("Please enter your number :"))
    
    if user_input%2 == 0:
        print("This is even number", user_input)
    else:
        print("This is odd number", user_input)
"""


############### use of and & or ################

# check the given can be divide by 3 and 5
"""
num1 = 18

if num1%3 == 0 and num1%5 == 0:
    print("number can be divide by 3 and 5 :", num1)
else:
    print("number can not be divide by 3 and 5 :", num1)
"""
# with or condition
"""
num1 = 22

if num1%3 == 0 or num1%5 == 0 :
    print("number can be divide by 3 or 5 :", num1)
else:
    print("number can not be divide by 3 or 5 :", num1)
"""

"""

and condition

True and True : True
False and True : False
True and False : False
False and False : False

or condition

True or True : True
True or False : True
False or True : True
False or False : False

"""

#########################if-elif-condition##########################

"""
if <condition>:
    code
elif <condition>:
    code
elif <condition>:
    code
else:
    code
"""

"""
num1 = 11

if num1%3 == 0:
    print("number can divide by 3 :", num1)
elif num1%5 == 0:
    print("number can divide by 5 :", num1)
elif num1%7 == 0:
    print("number can divide by 7 :", num1)
else:
    print("the number can not divide by 3, 5, or 7 :", num1)
"""

# check which is greater number among given three numbers
"""
# a = 40
# b = 50
# c = 70


a = 60
b = 100
c = 100


if a >= b and a >= c:  # 100 >= 100 : False and 100 > 70 : True = False
    print("a has greater value :", a)
elif b >= a and b >= c: # 100 > 100 : False and 100 > 70 : True = False
    print("b has greater value :", b)
elif c >= a and c >= b : # 70 > 100 : False and 70 > 100 : False = False
    print("c has greater value :", c)
else:
    print("We are in else condition")
"""

####################################### Nested If Condition #####################

"""
if <condition1>:
    code
    if <condition2>:
        code
        if <condition3>
            code
        else:
            code
    else:
         code
else:
    code

"""
"""

round1 = 'clear'
round2 = 'clear'
round3 = 'clear'

if round1 == 'clear':
    print("Congratulation your first round is clear")
    if round2 == 'clear':
        print("Congratulation your second round is clear")
        if round3 == 'clear':
            print("Congratulations, your are selected")
        else:
            print("Sorry, better luck next time, third round is not clear")
    else:
        print("Sorry, better luck next time, second round is not clear")
else:
    print("Sorry, better luck next time, first round is not clear")
"""

"""
# Check user authentication with credentials
db_username = 'vishal123'
db_password = 'P@ssw0rd'

username_input = 'vishal123'
password_input = 'P@ssw0rd'


if username_input == db_username:
    if password_input == db_password:
        print("Authentication is successful")
    else:
        print("Access Denied, password is not correct")
else:
    print("Access denied, username is not correct")

"""

# HW : write a python program to create a calculator which has option
# addition
# multiplication
# subtraction
# divide
# on the basic of choice

print("Please enter your choice :\n"
      "1. Addition \n"
      "2. Multiplication \n"
      "3. Subtraction \n"
      "4. Divide")









