low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:
    guess = (low + high) // 2

    print("Computer guess:", guess)
    ch = input("Enter (h = Higher, l = Lower, c = Correct): ")

    if ch == 'c':
        print("Computer guessed correctly!")
        break

    elif ch == 'h':
        low = guess + 1

    elif ch == 'l':
        high = guess - 1

    else:
        print("Invalid choice")

else:
    print("Your answer is not valid!")