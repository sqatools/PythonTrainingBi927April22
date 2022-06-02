emp_details = [[1,'santosh','san@123',9284978456,'pune'],[2,'pratik','prat@123',9284972556,'satara'],
               [3,'rushikesh','rushi@123',9284978411,'aurangabad'],[4,'deepak','deep@123',9284971456,'aurangabad'],
               [5,'pooja','pooja@123',9284978433,'nashik']]
while True:
    print('welcome to employee managerment system')
    print('1. to add employee')
    print('2. to remove employee')
    print('3. to show employee details usind id')
    print('4. to show all employee details')
    input1 = int(input('please choose any option 1-4 :'))
    if input1 == 1:
        a1 = int(input('please enter employee id :'))
        a2 = input('please enter name of employee :')
        a3 = input('enter email id :')
        a4 = int(input('enter mobile number of employee :'))
        emp_details.append(a1)
        emp_details.append(a2)
        emp_details.append(a3)
        emp_details.append(a4)
        print('Employees added to list successfully')
        print(emp_details)
    elif input1 == 2:
        print(emp_details)
        num = int(input('enter employee id to be removed :'))
        for i in emp_details:
            if num == i[0]:
                emp_details.pop(num-1)
            else:
                continue
        print('employee with employee is ',num,'is removed sucessfully')
        print(emp_details)
    elif input1 == 3:
        num = int(input('please enter employee id of whom you want details :'))
        for i in emp_details:
            if num == i[0]:
                print(emp_details[num-1])
            else:
                continue
    elif input1 == 4:
        print(emp_details)
