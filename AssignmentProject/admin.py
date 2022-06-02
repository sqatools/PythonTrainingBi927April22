import os
import json
from faker import Faker
from datetime import datetime
"""
pip install faker
"""
fake = Faker()

cur_path = os.getcwd()

def add_courses(course_file=os.path.join(cur_path, 'courses.txt')):
    course_id = 1
    try:
        if os.path.isfile(course_file):
            with open(course_file, "rb") as file:
                file_data = file.readlines()
                if file_data != []:
                    last_line = file_data[-1]
                    last_line_dict = json.loads(last_line)
                    last_id = last_line_dict['course_id']
                    course_id = int(last_id.split("_")[1])
                    new_course_id = f"course_{course_id+1}"
                else:
                    new_course_id = f"course_{course_id}"

        else:
            new_course_id = f"course_{course_id}"

        course_name = input("Please enter course name :")
        course_fee = input("Please enter course fee amount :")
        course_duration = input("Please enter course duration :")
        course_seats = input("Please enter total seats for the course :")
        total_registration = ""
        course_instructor = fake.user_name()
        review_rating = 1
        course_data = {
            "course_id" : new_course_id,
            "course_name" : course_name,
            "course_fee" : course_fee,
            "course_duration" : course_duration,
            "course_seats" : course_seats,
            "total_registration" : total_registration,
            "course_instructor" : course_instructor,
            "review_rating" : review_rating
        }

        new_data = json.dumps(course_data)
        with open(course_file, "a") as a_file:
            a_file.write(f"{new_data}\n")
    except Exception as e:
        print("Issue with File permission")
        raise e

def add_students(student_file = os.path.join(cur_path, 'student.txt')):
    student_data = {}

    while True:
        flag = True
        new_user_name = input("Please enter your username :")
        if os.path.isfile(student_file):
            with open(student_file, "rb") as file:
                file_data = file.readlines()
                if file_data != [] :
                    for line in file_data:
                        line_dict = json.loads(line)
                        user_name = line_dict['user_name']
                        if user_name == new_user_name:
                            print(f"Username {new_user_name} already taken")
                            flag = False
                else:
                    student_data['user_name'] = new_user_name
                    break
        if flag:
            student_data['user_name'] = new_user_name
            break
        else:
            continue

    password = input("Please enter password :")
    first_name = input("Please enter first name :")
    if first_name == "":
        first_name = fake.first_name()
    last_name = input("Please enter last name :")
    if last_name == "":
        last_name = fake.last_name()
    email = input("Please enter student email :")
    if email == "":
        email = fake.email()
    course = input("Please enter course name :")
    registration_date = datetime.now().strftime("%d/%m/%Y_%H_%M_%S")
    address = input("Please enter student address :")
    if address == "":
        address = fake.address()
    student_data["password"] = password
    student_data["first_name"] = first_name
    student_data["last_name"] = last_name
    student_data["email"] = email
    student_data["course"] = course
    student_data["registration_date"] = registration_date
    student_data["address"] = address
    student_data["user_type"] = "student"
    student_data_str = json.dumps(student_data)
    with open(student_file, "a") as a_file:
        a_file.write(f"{student_data_str}\n")

def add_instructor(instructor_file = os.path.join(cur_path, 'student.txt')):
    instructor_data = {}

    while True:
        flag = True
        new_user_name = input("Please enter your username :")
        if os.path.isfile(instructor_file):
            with open(instructor_file, "rb") as file:
                file_data = file.readlines()
                if file_data != [] :
                    for line in file_data:
                        line_dict = json.loads(line)
                        user_name = line_dict['user_name']
                        if user_name == new_user_name:
                            print(f"Username {new_user_name} already taken")
                            flag = False
                        else:
                            instructor_data['user_name'] = new_user_name
                            break
        if flag:
            instructor_data['user_name'] = new_user_name
            break
        else:
           continue

if __name__ == '__main__':
    add_students()