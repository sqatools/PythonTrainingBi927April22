"""
Method Overloading : When one class have two method with same name with different parameters:
Python does not support method overloading.
"""

# parent class
class company:
    """
    This is company class which takes two parameters which is
    company name and company address
    """
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show_company_details(self):
        print(f"Company : {self.name}\n"
              f"Address : {self.address}")

    # Method overloading is not available in python, it always consider latest defined method.
    # def show_msg(self, msg : str):
    #     print(msg)

    def show_msg(self, num1 : int, num2: int):
        """
        This method shows a msg to user
        :param num1: this first parameter of the function
        :param num2: this second parameter of the function
        :return:
        """
        print(num1, num2)

if __name__ == '__main__':
    obj = company('TCS', 'Hinjewadi')
    #obj.show_msg("Hello")

    print(dir(obj))
    print(obj.__module__)
    print(obj.__class__)
    print(obj.__doc__)
    print(obj.show_msg.__doc__)

