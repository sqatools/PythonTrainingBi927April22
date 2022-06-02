import json

with open("userd_data.txt", "r") as file:
    file_data = file.readlines()

    print(file_data)
    line1 = file_data[0]
    line_dict = json.loads(line1)
    print(line_dict['username'])