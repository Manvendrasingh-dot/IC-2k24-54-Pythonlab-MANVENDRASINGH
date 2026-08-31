n = int(input("Enter number of terms: "))


a = 0
b = 1
loop_series = []

for i in range(n):
    loop_series.append(a)
    a, b = b, a + b

print("Loop version:", loop_series)


count = 0

def fib(n):
    global count
    count += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

recursive_series = []
for i in range(n):
    recursive_series.append(fib(i))

print("Recursive version:", recursive_series)
print("Total recursive calls:", count)