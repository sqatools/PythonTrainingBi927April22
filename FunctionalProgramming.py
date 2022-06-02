"""
def function_name():
    code
"""

def function1():
    print("Hello Ram, How Are you ?")

# function1()
# function1()
# function1()
# function1()

def function2(name):
    print(f"Hello {name}, How are you?")


# function2('Ram')
# function2('Rishi')
# function2('Pratik')

def function3(num1, num2):
    print("num1 :", num1)
    print("num2 :", num2)
    print("Addition :", num1+num2)


# pass by value
function3(20, 30)

# pass by reference

number1 = 40
number2 = 60
function3(number1, number2)
print("_"*40)
# call paramters name

#function3(num1=60, num2=50)
print("_"*40)
#function3(num2=30, num1=80)
print("_"*40)
# error with extra parameter

#function3('90', 50, 80)

# Assign default values to the functions parameteres

def function4(var1=20, var2=60):
    print("var1:", var1)
    print("var2:", var2)

print("_"*40)
function4(50)
print("_"*40)
function4(5, 80)
print("_"*40)
function4(var2 = 70, var1=100)
print("_"*40)
function4()
print("_"*40)
function4('Python', 'Programs')


def function5(var1:int, var2:str):
    print("var1:", var1)
    print("var2:", var2)
    print(var1+var2)


#print("_"*40)
#function5('Hello', 567)
#print("_"*40)
#function5("Good ", "Morning")

def addition(num1=50, num2=60):
    return num1 + num2

output = addition(40, 60)

print("output :", output)

def multiply(num3):
    output = addition()
    result = output*num3
    return result

result = multiply(70)
print(result)

print("_"*40)

################# Function with *args #############

def function7(*args):
    for var in args:
        print(var)

#function7(6, 4, 7, 'm3', 8,'l', 3, 45, 4, 4, 65, 54,6 )
#function7('Ram', 'ram@gmail.com', 'Data Analyst', '50000')

def function8(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


#function8(name='Ram', email='ram@gmail.com', mobile=456345, salary=100000, job_title='Data Analytics')


def validate_login(**kwargs):
    db_username = 'admin'
    db_password = 'P@ssw0rd'
    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login Successful")
    else:
        print("Access Denied")

#validate_login(username='Admin', password='admin@123')
#validate_login(username='admin', password='P@ssw0rd')

