# Try A Guess game program

secret_number = 7
guess_chance = 0

while guess_chance < 3:
    guess_number = int(input("Guess a Secret number between 1 to 9: "))
    if guess_number == secret_number:
        print("You Win !!!")
        break
    elif guess_number != secret_number:
        print("You missed a chance" + "\n" + "Try Again")
        guess_chance += 1
else:
    print("You lost the Game. Better luck next time.")
