# multiplication_table.py

# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table from 1 to 10
for n in range(1, 11):
    result = number * n
    print(f"{number} * {n} = {result}")



