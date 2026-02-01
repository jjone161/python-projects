# Let's build a to-do list to track the errands we need to run
to_do = []    # to-do list which we will populate

# variable that continues the to-do app loop while true
errands = True 

# while loop for the logic for the to-do list
while errands == True:
    # show the users the options for the to-do 
    print("Hi there, thanks for using the to-do list")
    print("Please press 1 to add an item to the list")
    print("Please press 2 to view current items in the list")
    print("Please press 3 to remove an item from the list")
    print("Please press 4 to quit the to-do list")
    # Ask the user to choose a number to continue
    user_choice = int(input("Please choose a number: "))
    # conditional logic to account for user numerical input
    if user_choice == 1:
        task = input("Enter the task: ")
        to_do.append(task)
    elif user_choice == 2:
        for i, task in enumerate(to_do):
            print(f"{i}. {task}")
    elif user_choice == 3:
        task_num  = int(input("Enter number item to be removed: "))
        removed = to_do.pop(task_num)
        print(f"{removed} has been removed from the list")
    else:
        errands = False
        print(f"Closing the to-do list....DONE!")




