# lets track our expenses

# dictionary to hold expenses
expenses = {}

# boolean to keep loop going
running = True

# loop for expense log logic
while running == True:
    print("1. Add an expense with a category like food, transport, etc")
    print("2. View all expenses")
    print("3. View total spent per category")
    print("4. Quit")
    # get user's choice
    user_choice = int(input("Select an option: "))
    # if user selects #1
    if user_choice == 1:
        category = input("Enter expense category: ")
        expense_amount = float(input("Enter expense amount: "))
        if category in expenses:
            expenses[category].append(expense_amount)
        else:
            expenses[category] = [expense_amount]
    elif user_choice == 2:
        for key, value in expenses.items():
            print(f"{key}: {value}")
    elif user_choice == 3:
        for key, value in expenses.items():
            total = sum(value)
            print(f"{key}: ${total}")
    else:
        running = False
        print("Goodbye!")