while True:
    print("\n1. Enter Student Details")
    print("2. View Student Grade")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "Fail"

        print("Student details saved")

    elif ch == 2:
        if 'name' in locals():
            print("Name:", name)
            print("Marks:", marks)
            print("Grade:", grade)
        else:
            print("Please enter student details first")

    elif ch == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")