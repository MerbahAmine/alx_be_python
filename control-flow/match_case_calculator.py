## match_case_calculator.py
## Prompt for user input
first_number = float(input("Enter the first number: ")) 
second_number = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")
## Perform the calculation using match-case
match operation :
    case "+":
        result = first_number + second_number
        print(f"The result is {result}")
    case "-":
        result = first_number - second_number
        print(f"The result is {result}")
    case "*":
        result = first_number * second_number
        print(f"The result is {result}")
    case "/":
         
        if (second_number==0):
            print("Cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"The result is {result}")
