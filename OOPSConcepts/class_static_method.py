
class company:
    _city = "Pune"
    __state = "Maharastra"
    country  = "India"

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def _show_company_details(self):
        print(f"Company : {self.name}\n"
              f"Address : {self.address}")

    def __show_msg(self):
        self._show_company_details()
        print("We are in company class")

    @classmethod
    def show_name(cls):
        print(cls.country)
        print(cls._city)
        print(cls.__state)

    @staticmethod
    def factorial(num):
        fact = 1
        for i in range(1, num+1):
            fact = fact *i
        return fact

    @staticmethod
    def print_table(num : int):
        for i in range(1,  11):
            print(i,"*", num, "=", i*num)


if __name__ == '__main__':
    obj = company("TCS", "Hinjewadi")
    obj.show_name()
    obj._company__show_msg()
    print(obj.factorial(5))
    print(company.factorial(5))
    obj.print_table(10)