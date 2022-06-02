"""
single under score (_) :
double under score (__) :


"""

# parent class
class company:
    _city = "Pune"
    __state = "Maharastra"
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def _show_company_details(self):
        print(f"Company : {self.name}\n"
              f"Address : {self.address}")

    def __show_msg(self):
        print("We are in company class")

# child class
class employee(company):
    def __init__(self, address, emp_name, name):
        super().__init__(name, address)
        self.emp_name = emp_name

    def show_employee_details(self):
        print(f"Company : {self.name}\n"
              f"Address : {self.address}\n"
              f"Emp_Name : {self.emp_name}")

    def show_msg(self):
        print("We are in employee class")


class job_title(employee):

    def __init__(self, address, emp_name, com_name, job_title):
        super().__init__(address, emp_name, com_name)
        self.job_title = job_title


    def profile_details(self):
        print("We need IT engineer")
        print("Job Title :", self.job_title)

    def show_msg(self):
        print("We are in job_title class")

if __name__ == '__main__':
    obj = company("TCS", "Hinjewadi")

    print(obj._city)
    print(obj._company__state)   # _classname__var/method

    obj._show_company_details()
    obj._company__show_msg()
