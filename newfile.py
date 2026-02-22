expenses = []
print("Welcome to expense tracker")

while True:
    print("=== Menu ===")
    print("1. Add your expense")
    print("2. View your expense")
    print("3. View your amount")
    print("4. Exit")

    choice = int(input("Enter number: "))

    if choice == 1:
        date = input("Enter a date: ")
        category = input("Enter a category: ")
        description = input("Enter short description: ")
        amount = float(input("Enter amount: "))

        expenses.append({
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        })
        print("Expense added successfully!")

    elif choice == 2:
        print("\nYour Expenses:")
        if not expenses:
            print("No expenses yet.")
        else:
            for exp in expenses:
                print(f"Date: {exp['date']}, Category: {exp['category']}, Description: {exp['description']}, Amount: {exp['amount']}")

    elif choice == 3:
        total = sum(exp["amount"] for exp in expenses)
        print(f"Total amount spent: {total}")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")