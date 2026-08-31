
matrix = []
print("Enter 3x3 matrix row by row (space-separated):")
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

# Display matrix
print("\nMatrix:")
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# Sum of all elements
total = 0
for row in matrix:
    for val in row:
        total += val
print("\nSum of all elements:", total)

#Sum of main diagonal
diag_sum = 0
for i in range(3):
    diag_sum += matrix[i][i]
print("Sum of main diagonal:", diag_sum)

# Largest and smallest element
largest = matrix[0][0]
smallest = matrix[0][0]
for row in matrix:
    for val in row:
        if val > largest:
            largest = val
        if val < smallest:
            smallest = val
print("Largest element:", largest)
print("Smallest element:", smallest)

# 5. Transpose
print("\nTranspose:")
for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()
