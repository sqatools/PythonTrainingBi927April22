"""
# program : Get all the palindrome string from the given list.

input_list = ['cac', 'hello', 'are', 'you', 'ara', 'beb']

# Program : Get longest word from the word list.

input = ['Python', 'Programming', 'is', 'good', 'language']

# Program : copy data from list1 to list2:

list1 = [5, 7, 3, 8, 9]
list2 = []

# output:
"""
"""
list2 = [5, 7, 3, 8, 9]
list1 = []
"""

# program : Get all the palindrome string from the given list.
"""
input_list = ['cac', 'hello', 'are', 'you', 'ara', 'beb']

for val in input_list:
    rev_val = val[::-1]
    if val == rev_val:
        print(val)
    else:
        continue
"""
# longest word from the given list

#input = ['Python', 'Programming', 'is', 'good', 'language']

"""
Step1 : Apply loop on input list 'for word in input'
Step2 : Get word length using len method. len(word)
Step3 : compare word_len and long_len values and if word_len is greater than
        assign value to long_len, assign word to long_word var.
Step4 : Long length and the word
"""
"""
long_len = 0
long_word = ''
# Step1 : Apply loop on input list 'for word in input'
for word in input:
    # Step2 : Get word length using len method. len(word)
    word_len = len(word)
    # step3 : Step3 : compare word_len and long_len values and if word_len is greater than
    #         assign value to long_len, assign word to long_word var.
    if word_len > long_len:
        long_len = word_len
        long_word = word
    else:
        continue

print("long length :", long_len)
print("long word :", long_word)


# Program3 : move data from list1 to list2:

list1 = [5, 7, 3, 8, 9]
list2 = []
temp = list1.copy()
for var in temp:
    pop_item = list1.pop(0)
    list2.append(pop_item)


print("List1 :", list1)
print("List2 :", list2)

"""
######################### Fruit Shope Management App #################
"""
fruit_list = [['Apple', 50], ['Pinapple', 20], ['Banana', 10], ['Lichi', 60]]

while True:
    print("Welcome to our system :")
    print("Please enter your options:")
    print("1. Sell Fruits")
    print("2. Add Fruits")
    print("3. Remove Fruits")

    owner_input = int(input("PLease select the option:"))

    if owner_input == 1:
        print("Please select fruits from menu")
        sn_no = 0
        for fruit in fruit_list:
            print(f"{sn_no}: {fruit[0]} : price :{fruit[1]}/kg")
            sn_no = sn_no+1

        fruit_input = int(input("Please enter any number to select the fruits:"))
        quantity = int(input("Please enter how many fruits you want :"))
        print(f"You have selected fruit : {fruit_list[fruit_input][0]}, and you want this {quantity} quantity")

        bill = fruit_list[fruit_input][1] * quantity
        print(f"Your bill is : {bill}")
        print("Please pay your bill and collect the fruits")

    if owner_input == 2:
        fruit_name = input("Please enter fruit name :")
        fruit_price = int(input("Please enter fruit price :"))
        fruit_list.append([fruit_name, fruit_price])
        print(f"Fruit  {fruit_name}, Successfully added to inventory")

        print("Updated fruit inventory")
        sn_no = 0
        for fruit in fruit_list:
            print(f"{sn_no}: {fruit[0]} : {fruit[1]}")
            sn_no = sn_no + 1

    print("_" * 20)
    print("____"*20)
    if owner_input == 3:
        print("Fruits Menu")
        sn_no = 0
        for fruit in fruit_list:
            print(f"{sn_no}: {fruit[0]} : {fruit[1]}")
            sn_no = sn_no + 1

        fruit_position = int(input("Please select fruit to remove from inventory :"))
        print(f"Fruit {fruit_list[fruit_position][0]} removed from the inventory")
        fruit_list.pop(fruit_position)
        print("_"*20)
        print("Updated fruit inventory")
        for fruit in fruit_list:
            print(f"{sn_no}: {fruit[0]} : {fruit[1]}")
            sn_no = sn_no + 1
    print("_" * 20)


############################

# Design a employee management tool
# -> Add employee (id, name, email, mobile, address)
# -> remove employee (id)
# -> Show employee details (id)
# -> Show all employee details
"""

list11 = [40, 30, 4, 6, 7]

print(max(list11))

print(min(list11))

print(sum(list11))





