def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice_input = input("Enter your choice: ")

        # convert input to number
        if choice_input.isdigit():
            choice = int(choice_input)
        else:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print("Item added.")

        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print("Item removed.")
            else:
                print("Item not found in the list.")

        elif choice == 3:
            if len(shopping_list) == 0:
                print("Shopping list is empty.")
            else:
                print("Your Shopping List:")
                for item in shopping_list:
                    print("- " + item)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
