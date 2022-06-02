"""
Inheritance : aquire the property of one class by another class

1: Single inheritance : A(parent) -> B (child)
2: Multi level inheritance :
A(parent) -> B(parent) -> C(last class)

3: Multiple Inheritance A-> B and C -> B
"""

# parent class
class company:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show_company_details(self):
        print(f"Company : {self.name}\n"
              f"Address : {self.address}")

# child class
class employee(company):
    def __init__(self, address, emp_name, name):
        super().__init__(name, address)
        self.emp_name = emp_name

    def show_employee_details(self):
        print(f"Company : {self.name}\n"
              f"Address : {self.address}\n"
              f"Emp_Name : {self.emp_name}")


class job_title(employee):

    def __init__(self, address, emp_name, com_name, job_title):
        super().__init__(address, emp_name, com_name)
        self.job_title = job_title


    def profile_details(self):
        print("We need IT engineer")
        print("Job Title :", self.job_title)

if __name__ == '__main__':
    obj = job_title("Mumbai", "John", "Facebook", "Software Developer")
    obj.profile_details()
