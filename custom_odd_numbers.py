# To print required number of odd numbers and find nth odd number

x = int(input("Required number of odd numbers: "))
a = 1
b = 2
k = []

print("Requested number of Odd Numbers are:")

for c in range(b):
    for i in range(x):
        b = a % 2
        if b != 0:
            print(a)
            k = a
        a += 1

print(str(x) + "/" + "nth ODD Number is: " + str(k))
