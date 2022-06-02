"""
#While Loop

while condition:
    code
"""

"""
num1 = 2

temp = 1

while temp < 11:
    print(temp*num1)
    temp = temp + 1
"""
"""
# factorial of given number
num3 = 5  # 5*4*3*2*1
fact = 1

while num3 > 0: #5
    fact = fact*num3
          # 1*5, 5*4, 20*3, 60*2 , 120*1, 120
    num3 = num3 - 1

print('factorial value :', fact)

"""
################################################
# Write infinite loop with while loop.
"""
temp = 0
while True:
    print("its continue loop :",  temp)
    if temp == 10:
        break
    else:
        temp = temp + 1
"""
################################

# Program 1: write a python program to get list of number which can divide 3 and 7 from 1 to 1000.
           # output  -> the number which are divide 3 and 7 as well as only even number.
# Program 2: Write a python program to get all the number which are multiple of 5 from 1 to 1000.
           #-> and those number should only contain 5 e.g  5, 55, 555
# Program 3: Write a python program to check given number is palindrome or not

#num1 = 234
#output : number is not palindrome

#num1 = 121
#output : number is  palindrome

"""
for i in range(1000):
    if i%5 == 0:
        temp = str(i)
        size_temp = len(temp)
        count5 = temp.count('5')
        if size_temp == count5:
            print(i)
        else:
            continue
"""

# to check given number is palindrome or not

"""
num1 = 123
new_num = num1
reverse_val = 0
while num1 > 0:
    temp = num1%10
    reverse_val = reverse_val*10 + temp
    num1 = num1//10

#print("reverse_value :", reverse_val)

if reverse_val == new_num:
    print("it is palindrome number :", new_num)
else:
    print("it is not palindrome number :", new_num)

"""

# get all the numbers which has same value in output
#import pdb; pdb.set_trace()
"""
mul_num = 8

for i in range(1, 10000):
    if i%mul_num == 0:
        #print(i)
        # i = 1, 2, 3, 4, 5, 11, 55, 110
        new_num = i
        flag = True
        while new_num > 0:
            temp = new_num % 10
            if temp == mul_num:
                new_num = new_num // 10
            else:
                flag = False
                break
        if flag:
            print(i)

"""
##################################################
# Program : write a python program to print this pattern

"""
    *         *
  * * *     * * *
* * * * * * * * * *
"""
#Program: write a python program to print given pattern

"""
2
4 6
8 10 12
14 16 18 20
22 24 26
28 30
32
"""

# Program : write a python program to print given pattern

""" 
        50
     40 45 3
  25 30 35 6 9
5 10 15 20 12 15 18
"""

"""
2
4 6
8 10 12
14 16 18 20
22 24 26
28 30
32
"""
"""
temp = 2
for i in range(1, 5):
    for j in range(i):
        print(temp, end=" ")
        temp = temp + 2
    print()

for k in range(4, 1, -1):
    for l in range(1, k):
        print(temp, end=" ")
        temp = temp + 2
    print()
"""



""" 
           50             

         45 40 3          

      35 30 25 6 9       

   20 15 10 5 12 15 18

"""

b1 = 3 #2 , 1
b2 = 5 #6 , 7
temp1 = 50
temp2 = 3
for i in range(4):
    for j in range(9):
        if j > b1 and j < b2:
            if j < 5:
                print(temp1 ,end=' ')
                temp1 = temp1 - 5
            else:
                print(temp2, end=' ')
                temp2 = temp2 + 3

        else:
            print(" ", end=' ')

    b1 = b1 - 1
    b2 = b2 + 1
    print("\n")




