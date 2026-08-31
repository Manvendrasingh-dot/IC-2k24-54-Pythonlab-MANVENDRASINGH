limit = int(input("Enter the limit: "))

print("Perfect numbers are:")

for n in range(1, limit + 1):
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        print(n)