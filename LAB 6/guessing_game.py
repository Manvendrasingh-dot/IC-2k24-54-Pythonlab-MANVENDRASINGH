import random

num = random.randint(1, 50)
score = 100

while score>0:
    guess = int(input("Guess any number from 1-50  "))

    if guess == num:
        print("Correct Guess!")
        print("Your score =", score)
        break

    else:
        score = score - 10

        if num % 2 == 0:
            print("Hint: Number is Even")
        else:
            print("Hint: Number is Odd")

        if num % 5 == 0:
            print("Hint: Number is a multiple of 5")
        else:
            print("Hint: Number is not a multiple of 5")

        print("Wrong Guess! Try again.")
        print("Remaining score =", score)
else:
    print("Bad Luck, No chance left !! try again")