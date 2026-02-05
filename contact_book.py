# let's build a contact book for our phone contacts

# empty dictionary for our contact 
contacts = {}

# variable to keep contact book active
running = True

# loop to show user all options for contact book
while running == True:
    # show user all options
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Look up a contact")
    print("4. Quit")
    # Ask user to make a selection
    user_choice = int(input("Please make a selection: "))
    if user_choice == 1:
        # Add a new contact
        contact_name = input("Contact name: ")
        contact_number = int(input("Enter 10 digit number: "))
        # adds a new contact by key and value to dict
        contacts[contact_name.lower()] = contact_number 

    elif user_choice == 2:
        # View all contacts
        for key, value in contacts.items():
            print(f"{key}: {value}")
    elif user_choice == 3:
        # Contact lookup
        contact_lookup = input("Enter name: ")
        if contact_lookup.lower() in contacts:
            print(contacts[contact_lookup.lower()])
        else:
            print("Sorry, Contact not found")
    else:
        running = False
        print("Closing contact book....Goodbye")

