# Different read operations

# Read specific number of character
"""
file = open("read_file11.txt", "r")
data = file.read(10)
print(data)
file.close()
"""

# Read single line
"""
file = open("read_file11.txt", "r")
data = file.readline()
print(data)
file.close()
"""

# read list of lines
"""
file = open("read_file11.txt", "r")
data = file.readlines()
print(data)
file.close()
"""
############### Read file with context  manager #######
"""
with open("read_file11.txt", "r") as file:
    data = file.readlines()
    print(data)
"""
"""
# Read last 2 lines of the file
with open("read_file11.txt", "rb") as file:
    # lines_list = file.readlines()
    # for i in range(-2, 0, 1):
    #     print(lines_list[i], end="")
    #

    lines_list = file.readlines()[-2:]
    for line in lines_list:
        print(line, end="")
        
"""
# write a python to count specific word occurance in the file
"""
def get_word_count(filepath, word):
    with open(filepath, "r") as file:
        data  = file.read()
        word_count = data.count(word)
    return word_count


filepath =  "read_file11.txt"
word = "Python"

output = get_word_count(filepath, word)
print(output)
"""


# Program : Get all even length and odd length words separately and write in two separate file
"""
def get_odd_even_words(filepath):
    odd_words = []
    even_words = []
    with open(filepath, 'r') as file:
        data = file.read()
        word_list = data.split(" ")
        for word in word_list:
            word_len = len(word)
            if word_len%2 == 0:
                even_words.append(word)
            else:
                odd_words.append(word)

    return odd_words, even_words


filepath =  "read_file11.txt"
odd_word, even_word = get_odd_even_words(filepath)
print(odd_word)
print(even_word)

odd_word_str = " ".join(odd_word)
print(odd_word_str)

even_word_str = " ".join(even_word)
print(even_word_str)


with open("odd_words.txt", "w") as file:
    file.write(odd_word_str)

with open("even_words.txt", "w") as file:
    file.write(even_word_str)
"""
# Write python code to replace word1 with word2

def replace_word(filepath, word1, word2):
    with open(filepath, "r") as file:
        file_data = file.read()
        new_data = file_data.replace(word1, word2)

    with open(filepath, "w") as file:
        file.write(new_data)

#filepath =  "read_file11.txt"
#replace_word(filepath, "Python", "Java")

# Write a python program to get all email from the

def get_email(filepath):
    email_list = []
    with open(filepath, "r", encoding='utf-8') as file:
        file_data = file.read()
        word_list = file_data.split(" ")
        for word in word_list:
            if "@" in word:
                email_list.append(word)
            else:
                continue
    print(email_list)


if __name__ == '__main__':
    filepath = "read_file11.txt"
    get_email(filepath)




