balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("Balance =", balance)

    elif ch == 2:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Money deposited successfully")

    elif ch == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Money withdrawn successfully")
        else:
            print("Insufficient balance")

    elif ch == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")