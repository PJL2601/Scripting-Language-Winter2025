# Expected Output: Print factorial of 5 (120)
n = 5
factorial = 1  # Initialize to 1, not 0
for i in range(1, n + 1):
    factorial *= i
print(factorial)
