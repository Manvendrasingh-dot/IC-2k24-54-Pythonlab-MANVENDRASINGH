n = int(input("Enter a number: "))

temp = n
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if n == reverse:
    print(n, "is a Palindrome")
else:
    print(n, "is not a Palindrome")


s = input("Enter a string: ")

if s == s[::-1]:
    print(s, "is a Palindrome")
else:
    print(s, "is not a Palindrome")