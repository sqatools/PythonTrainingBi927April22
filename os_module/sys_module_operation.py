import sys

print(sys.version_info)
print(sys.platform)
print(sys.getwindowsversion())

print(sys.argv)


def login(user_name, password):
    db_username = "admin"
    db_password = "P@ssword"
    if user_name == db_username and password == db_password:
        print("Login successful")
    else:
        print("Login failed")

user_name = sys.argv[1]
password = sys.argv[2]

login(user_name, password)