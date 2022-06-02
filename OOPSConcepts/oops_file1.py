"""
class : class is nothing but a blue print of the object
object : object through which we can use all the properties of the file.
inheritance
polymorphism
incapsulation
"""
class car:

    # class variable
    car_prize = 40000

    # Parametize constructor
    def __init__(self, carname, company):
        # instance variable
        self.carname = carname
        self.company = company

    # Instance Method
    def show_car_name(self):
        print("This is Tata Nexon Car")

    def show_company_name(self):
        print(f"This my first car, company: {self.company}")


if __name__ == '__main__':
    obj = car("Harrier", "Tata Motors")
    obj.show_car_name()
    obj.show_company_name()
    print(obj.__module__)
    print(obj.company)
    print(obj.carname)
    print(obj.car_prize)



