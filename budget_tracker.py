# building a budget tracker for our groceries 

items = []

# our total amount spent (starting at 0)
total = 0 

# boolean to keep our loop going
shopping = True

# while loop for tracker logic
while shopping == True:
    print("please enter an item or type quit to exit")
    item_name = input("Name of the item: ")
    if item_name == "quit":
        shopping = False
        print("Closing the tracker...")
    else:
        # only ask for price if they dont quit
        item_price = float(input("Enter price: "))
    # add name of item to list
        items.append(item_name)
    # add cost of item to our total 
        total += item_price
    # show user's current total 
        print(f"Your current total is ${total:.2f}")
    # show current items
        print(f"Purchased items: {items}")
    