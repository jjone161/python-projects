# Creating a recipe book to store recipes

# dictionary to hold recipe names. Each name will have a list of ingredients
recipe = {}

# Boolean to keep loop running
running = True

# While loop for recipe book logic
while running == True:
    # show users possible selections
    print("1. Add a new recipe")
    print("2. Add an ingredient to existing recipe")
    print("3. View a recipe's ingredients")
    print("4. View all recipes")
    print("5. Quit")
    # ask user for their choice
    user_choice = int(input("Select a number: "))
    # if user selects # 1
    if user_choice == 1:
        recipe_name = input("Enter recipe name: ")
        recipe[recipe_name.lower()] = []
    # if user selects # 2
    elif user_choice == 2:
        which_recipe = input("Enter name of recipe: ")
        ingredient = input("Enter ingredient: ")
        recipe[which_recipe.lower()].append(ingredient)
    # if user selects # 3
    elif user_choice == 3:
        view_recipe = input("Enter recipe name: ")
        if view_recipe.lower() in recipe:
            print(f"{recipe[view_recipe.lower()]}")
        else:
            print("Recipe not found")
    # if user selects # 4
    elif user_choice == 4:
        for key in recipe:
            print(key)
    # if user selects # 5
    else:
        running = False
        print("goodbye!")
