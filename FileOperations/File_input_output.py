"""
file = open(filepath, file_mode)
data = file.read()
print(data)

file_mode
r : read mode
We can read the existing available in the system.

w : write mode
a : append mode
"""

################ Read file #######################
"""
#file = open("read_file.txt", "r")

file_obj = open("E:\\Filesdata\\file1.txt", "r")
data = file_obj.read()
print(data)

print(file_obj.name)
print(file_obj.mode)
file_obj.close()
"""

################ Write content to the file ######################
"""
When ever we open file with write mode and add some content to the file, it overwrite existing content.
and if file is not available, then it will new file and add data to it.
"""
"""

str1 = "Its nice day"

file1 = open("write_file.txt", "w")
file1.write(str1)
file1.close()

# Create new file
str1 = "Its nice day,  happy learning to all"
file1 = open("write_file1.txt", "w")
file1.write(str1)
file1.close()
"""

############################### Append data to the file ##########################
"""
-> If file not available it, will create file
-> It add the content to the end of existing file.
"""
"""

str1 = "\nthis data will be appeded to the end of the file"
file1 = open("append_file1.txt", "a")
file1.write(str1)
file1.close()

str2 = "\nfresh data adding to new file"
file2 = open("append_file_new.txt", "a")
file2.write(str1)
file2.close()
"""

"""
file3 = open("html_file2.html", "w")
data = file3.write("<html><head><title>Python</title><body>Its python page</body></html>")
print(data)

"""
"""
str1 = "Its nice day"

file1 = open("write_file.txt", "w")
output = file1.write(str1)
print(output)
file1.close()
"""

#################### Get cursor location will tell method #########
"""
with open("read_file11.txt", "r") as file:
    print(file.tell())
    data = file.read(10)
    print(data)
    print(file.tell())

    data1 = file.read(10)
    print(data1)

    print(file.tell())

    data2 = file.readline()
    print(data2)
    print(file.tell())
"""
#####################Read data from specific position ################



with open("read_file11.txt", "rb") as file:

    """
    # scenario 1 : cursor jump from initial position
    print(file.tell())
    file.seek(20, 0)
    print(file.tell())
    data = file.readline()
    print(data)
    """

    # scenario 2:  cursor jump from current cursor position
    """
    print("initial :", file.tell())
    data = file.read(10)
    print("after 10 byte read :", file.tell())
    file.seek(20, 1)
    print("after 20 byte jump from current postion :", file.tell())
    
    """


    #scenario 3: set cursor pointer end of the file
    file.seek(-10, 2)
    print("after -10 byte :", file.tell())
    data = file.readline()
    print(data)
    print("after read line:", file.tell())









