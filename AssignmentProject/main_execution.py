import os
import json
from AssignmentProject.admin import *

cur_dir = os.getcwd()
admin_file_path = os.path.join(cur_dir, 'admin.txt')
student_file_path = os.path.join(cur_dir, 'student.txt')
instructor_file_path = os.path.join(cur_dir, 'instructor.txt')
users_files = [admin_file_path, student_file_path,  instructor_file_path]

def login(user_name, password):
    login_flag = False
    user_type = None
    for file_name in users_files:
        with open(file_name, "r") as file_obj:
            file_data = file_obj.readlines()
            for file_line in file_data:
                #print(file_line)
                line_dict = json.loads(file_line)
                file_user_name = line_dict["user_name"]
                file_password  = line_dict["password"]
                user_type = line_dict["user_type"]
                if file_user_name == user_name and file_password == password:
                    login_flag = True
                    return login_flag, user_type
                else:
                    continue
    return login_flag, user_type


def main():
    while True:
        print("Please Enter you username and password :")
        user_name = input("Username :")
        password = input("Password :")
        login_flag, user_type = login(user_name, password)
        if login_flag is True and user_type == "Admin":
            print(f"Login Success Successful, You have {user_type} permissions")
            while True:
                print("Please select task number:\n"
                      "1. Add Student\n"
                      "2. Add Instructor\n"
                      "3. Add Courses \n"
                      "4. View Students \n"
                      "5. View Instructor \n"
                      "6. View Courses \n"
                      "7. Logout From Admin")

                user_input = input("task number :")
                if user_input == '1':
                    add_students()
                    print("Student Added Successfully")
                elif user_input == '2':
                    add_instructor()
                elif user_input == '3':
                    add_courses()
                    print("Course Added Successfully")
                elif user_input == '7':
                    print("Logged out from Admin")
                    print("__"*50)
                    break
        elif login_flag is True and user_type == "student":
            print(f"Login Success Successful, You have {user_type} permissions")
        elif login_flag is True and user_type == "instructor":
            print(f"Login Success Successful, You have {user_type} permissions")
        print("__" * 50)
if __name__ == '__main__':
    main()

# login_flag,  user_type = login("trainer201", "P@ssw0rd")
# if login_flag:
#     print(f"Login Success Successful, You have {user_type} permissions")
# else:
#     print("Username or Password is Wrong")
#




