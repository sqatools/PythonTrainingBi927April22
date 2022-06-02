"""
try:
  code
except:
   msg
"""
"""
try :
    num1 = 40
    num2 = "Hello"

    print(num1+num2)
except Exception as e:
    print("We can not add int and string")
    print(e)

"""

# Exception with Else Condition
"""
try :
    num1 = 40
    num2 = 2

    print(num1//num2)
except Exception as e:
    print("Can not divide number by 0")
    print(e)
else:
    print("We are learning exception")
"""
# Finally concept in except handling
"""
num = 31
try :
    div_num = 0
    print(num//div_num)
except Exception as e:
    print("Can not divide number by 0")
    #print(e)
finally:
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
        else:
            continue

    if flag:
        print("prime number :", num)
    else:
        print("this is not an prime number :", num)

"""

# Exception with else and Finally condition

num = 21
num3 = 40
try :
    div_num = 3
    print(num//div_num)
    assert num == num3
except Exception as e:
    print("Can not divide number by 0")
    #raise e
else:
    print("There is no exception")
finally:
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
        else:
            continue

    if flag:
        print("prime number :", num)
    else:
        print("this is not an prime number :", num)


