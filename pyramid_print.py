# Print pyramid shape as per the mentioned number of layers/height


x = int(input("Number of layers: "))

for a in range(x):
    if a == 0:
        space = x - (a + 1)
        pyramid = a + 1
        print("\n" + space * " " + pyramid * "*")

    else:
        space = x - (a + 1)
        pyramid = a + a + 1
        print(space * " " + pyramid * "*")
print("\n" + "😊 Success !!! 👍")
