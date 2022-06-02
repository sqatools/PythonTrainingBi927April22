school = {

    'student' : [
                  {'name' : 'stud1', 'email': 'stud1@gmail.com', 'mobile' : 42234},
                  {'name' : 'stud2', 'email': 'stud2@gmail.com', 'mobile' : 454234},
                  {'name' : 'stud3', 'email': 'stud3@gmail.com', 'mobile' : 451234},
                  {'name' : 'stud4', 'email': 'stud4@gmail.com', 'mobile' : 456234},
                  {'name' : 'stud5', 'email': 'stud5@gmail.com', 'mobile' : 463543234},
                 ],
     'teachers' : [
                    {'name' : 'teach1', 'email': 'teach1@gmail.com', 'mobile' : 42256543},
                    {'name' : 'teach2', 'email': 'teach2@gmail.com', 'mobile' : 42256543},
                    {'name' : 'teach3', 'email': 'teach3@gmail.com', 'mobile' : 42445433},
                    {'name' : 'teach4', 'email': 'teach4@gmail.com', 'mobile' : 422333654},
                    {'name' : 'teach5', 'email': 'teach5@gmail.com', 'mobile' : 422533654},
                ]

}


def get_student_mobile_number(stu_name):

    for data in school['student']:
        if data['name'] == stu_name:
            return data['mobile']
        else:
            continue

def get_student_email_number(stu_name):

    for data in school['student']:
        if data['name'] == stu_name:
            return data['email']
        else:
            continue
#mobile_number = get_student_mobile_number('stud5')
#email = get_student_email_number('stud5')
#print(mobile_number, email)


def get_student_details(stu_name):
    mobile_number = get_student_mobile_number(stu_name)
    email = get_student_email_number(stu_name)
    print('Student Name :', stu_name)
    print("Student Mobile Number :", mobile_number)
    print("Student Email ID :", email)

list_stu = ['stud3', 'stud4', 'stud5']

# for name in list_stu:
#     get_student_details(name)
#     print("__"*20)

def add_student_details(**kwargs):
    school['student'].append(kwargs)
    for data in school['student']:
        print(data)

def remove_student_data(stu_name):
    for data in school['student']:
        if data['name'] == stu_name:
            school['student'].remove(data)
        else:
            continue

    for data in school['student']:
        print(data)



#add_student_details(name='stud6', email='stud6@gmail.com', mobile=985623452, city='Pune')
#print("__" * 20)
#add_student_details(name='Pratik', email='Pratik@gmail.com', mobile=982613435, city='Mumbai')