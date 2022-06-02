# Scope of the variables
"""
global : scope of this variable is global , al the function in the module can use it directly.
local : this variable defined inside the function and its scope is limited to the function only.
non local : this variable defined outside of inner functions and its scope is limited to all the
            inner functions.
"""

# global variable
var1 = 100
varp = 200

def function1():
    print("function1")
    # local variable
    var2 = 50
    print("var2 :", var2)
    print("var1 :", var1)
    print("varp :", varp)

def function2():
    print("function2")
    global var1, varp
    var3 = 60
    var1 = 150
    varp = 500
    print("var1 :", var1)
    #print("var2 :", var2)
    print("var3 :", var3)
    print("varp :", varp)

def function3():
    print("function3")
    var4 = 70
    print("var1 :", var1)
    print("var4 :", var4)
    print("varp :", varp)

# function1()
# print("*"*50)
# function2()
# print("*"*50)
# function3()
# print("*"*50)
# function1()


# global variable
varp = 200

def outer_fuction():
    # non local variable
    varq = 300

    def inner_function1():
        print("inner function1")
        vars = 100 # local variable
        print("varp :", varp)
        print("varq :", varq)
        print("vars :", vars)

    def inner_function2():
        print("inner function2")
        vart = 180 # local variable
        nonlocal varq
        varq = 900
        global varp
        varp = 1000
        print("varp :", varp)
        print("varq :", varq)
        print("vart :", vart)

    inner_function1()
    print("*"*50)
    inner_function2()
    print("*" * 50)
    inner_function1()

#outer_fuction()


################ pass #######################

def new_function():
    pass