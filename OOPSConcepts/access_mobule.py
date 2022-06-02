from OOPSConcepts.class_static_method import company

#obj = company("TCS", "Hinjewadi")

#print(obj.factorial(6))

class A:
    def __init__(self):
        self.obj = company("TCS", "Hinjewadi")

    def show_msg_A(self):
        self.obj._company__show_msg()

if __name__ == '__main__':
    obja = A()
    obja.show_msg_A()
