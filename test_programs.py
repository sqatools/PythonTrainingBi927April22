counter = 0
with open("Day1.txt", "r") as file:
    data = file.read()
    for char in data:
        if char.isupper():
            counter = counter + 1
        else:
            continue

print(counter)