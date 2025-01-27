# Expected Output: Keep asking until the user enters a positive number
while True:
    try:
        number = int(input("Enter a positive number: "))
        if number >= 0:
            break
        print("Please enter a positive number!")
    except ValueError:
        print("Please enter a valid number!")
print("Thank you!")
