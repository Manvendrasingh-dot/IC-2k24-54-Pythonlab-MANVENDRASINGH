limit = int(input("Enter the limit: "))

print("Prime numbers are:")

for n in range(2, limit + 1):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print(n)
        