def hollow_diamond(n):
    mid = n // 2
    for i in range(mid + 1):
        if i == 0:
            print(" " * mid + "*")
        else:
            print(" " * (mid - i) + "*" + " " * (2 * i - 1) + "*")
    for i in range(mid - 1, -1, -1):
        if i == 0:
            print(" " * mid + "*")
        else:
            print(" " * (mid - i) + "*" + " " * (2 * i - 1) + "*")

hollow_diamond(7)
print()

def butterfly(n):
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    for i in range(n - 1, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

butterfly(5)