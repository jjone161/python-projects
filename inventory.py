# tracker to track store inventory

# dictionary to store inventory
inventory = {}      # we will add items later

# boolean to keep loop runnning
running = True

# loop for tracker logic
while running == True:
    # show user options
    print("1. Add a new item with starting quantity")
    print("2. Add more stock to an existing item")
    print("3. View all inventory")
    print("4. Quit")
    # get user choice
    user_choice = int(input("Please choose a number: "))
    # user choice 1
    if user_choice == 1:
        item_name = input("Enter item name: ")
        item_quantity = int(input("Enter number of items: "))
        inventory[item_name.lower()] = item_quantity
    # user choice 2
    elif user_choice == 2:
        which_item = input("Enter item name to update: ")
        new_quantity = int(input("Enter number of stock to add: "))
        inventory[which_item.lower()] += new_quantity 
    # user choice 3
    elif user_choice == 3:
        for key, value in inventory.items():
            print(f"{key}: {value}")
    # user choice 4
    else:
        running = False
        print("Goodbye!")