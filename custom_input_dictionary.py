# get custom inputs and create a dictionary

elements = int(input("Number of Elements: "))

Dict = {}

for i in range(elements):

    key = input("Enter KEY: ")
    typ1 = input("Is the entered KEY a Number? give 'y/n': ")

    if typ1.lower() == "y":
        key = int(key)

    elif typ1.lower() == "n":
        key = str(key)

    else:
        print("Invalid input try again")

    value = input("Enter Value: ")
    typ2 = input("Is the entered VALUE a Number? give 'y/n': ")

    if typ2.lower() == "y":
        value = int(value)

    elif typ2.lower() == "n":
        value = str(value)

    else:
        print("Invalid input try again")

    Dict[key] = value

print(Dict)
