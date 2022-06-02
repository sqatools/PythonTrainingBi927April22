import os
import shutil

# get current directory
print(os.getcwd())

# Read environment variable
print(os.getenv("path"))
print(os.getenv("Browser"))

# Get list of all files and folders
files_list = os.listdir("E:\\Filesdata")
print(files_list)

# join two path with join method
tar_dir = "E:\\Filesdata"
filename = "count_name.txt"
new_dir = "new_dir1"

file_path = os.path.join(tar_dir, filename)
print(file_path)

folder_path = os.path.join(tar_dir, new_dir)
print(folder_path)

# check if file and folder exist or not

print("file availability :", os.path.isfile(file_path))
print("folder availability :", os.path.isdir(folder_path))


# Create directory on target
#os.mkdir(folder_path)

# remove directory/files from target

#os.removedirs(folder_path)  # it removes the directory from path
#os.remove(file_path)        # it removes the files from path

# execute local command

"""
os.system('appwiz.cpl')
os.system('control')
os.system('dir')
os.system('notepad.exe')
"""

# copy file from one location to another location
src_path = "E:\\Filesdata\\count_name.txt"
tar_path = "E:\\Filesdata\\new_dir\\count_name.txt"
shutil.copy(src_path, tar_path)
