 from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    days_input = input("Enter the number of days to add to the current date: ")
    if days_input.isdigit():
        number_of_days = int(days_input)
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    else:
        print("Invalid input. Please enter a number.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
