# pattern_drawing.py
# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))
# Initialize the row counter
row = 0
# Use a while loop to iterate over each row
while row < size:
    # Use a for loop to print asterisks for each column in the row
    for col in range(size):
        print("*", end="")
    # After printing all columns in a row, print a newline
    print()
    # Increment the row counter
    row += 1
