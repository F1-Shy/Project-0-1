# Personal Expense Tracker

# Global variables
total_expenses = 0
expenses_list = []
categories_dict = {}


def display_menu():
    """Show the menu and get user choice"""
    print("\n=== Personal Expense Tracker ===")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. View summary by category")
    print("4. Search expenses")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number 1–5.")
        return None


def add_expense():
    """Add a new expense"""
    global total_expenses

    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter expense category: ")

    # Add expense to list
    expenses_list.append({"name": name, "amount": amount, "category": category})

    # Update dictionary
    if category not in categories_dict:
        categories_dict[category] = []
    categories_dict[category].append(amount)

    # Update total
    total_expenses += amount

    print("Expense added successfully!")


def view_all_expenses():
    """Display all expenses"""
    if not expenses_list:
        print("No expenses recorded.")
    else:
        print("\n=== All Expenses ===")
        for i, expense in enumerate(expenses_list, start=1):
            print(f"{i}. {expense['name']} - ${expense['amount']:.2f} ({expense['category']})")


def view_summary_by_category():
    """Display total spent by category"""
    if not categories_dict:
        print("No category data available.")
    else:
        print("\n=== Summary by Category ===")
        for category, amounts in categories_dict.items():
            total = sum(amounts)
            print(f"{category}: ${total:.2f}")


def search_expenses():
    """Search for expenses by name"""
    keyword = input("Enter search keyword: ").lower()
    found = False

    print("\n=== Search Results ===")
    for expense in expenses_list:
        if keyword in expense['name'].lower():
            print(f"{expense['name']} - ${expense['amount']:.2f} ({expense['category']})")
            found = True

    if not found:
        print("No expenses matched your search.")


def main():
    """Main program loop"""
    while True:
        choice = display_menu()
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_all_expenses()
        elif choice == 3:
            view_summary_by_category()
        elif choice == 4:
            search_expenses()
        elif choice == 5:
            print("Goodbye! Thanks for using the tracker.")
            break
        elif choice is None:
            continue
        else:
            print("Invalid choice. Please enter a number 1–5.")


# Run the program
if __name__ == "__main__":
    main()
