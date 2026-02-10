# let's create a Movie Ratings Tracker

# empty dictionary to hold our movies
movies = {}

# boolean to keep loop running
running = True

# while loop for movie rating tracker logic
while running == True:
    # show user options
    print("1. Add a new movie with rating")
    print("2. Update an existing movie's rating")
    print("3. View a specific movie's ratings")
    print("4. View all movies and ratings")
    print("5. Quit")
    # get the user's choice
    user_choice = int(input("Please choose a number: "))
    # if user selects # 1
    if user_choice == 1:
        movie_name = input("Enter movie name: ")
        movie_rating = int(input("Enter movie rating 1 - 5: "))
        movies[movie_name.lower()] = movie_rating
    # if user selects # 2
    elif user_choice == 2:
        which_movie = input("Enter movie name: ")
        new_rating = int(input("Enter new rating: "))
        movies[which_movie.lower()] = new_rating 
    # if user selects # 3
    elif user_choice == 3:
        view_rating = input("Enter movie name: ")
        if view_rating.lower() in movies:
            print(movies[view_rating.lower()])
        else:
            print("Movie not found")
    # if user selects # 4
    elif user_choice == 4:
        print(movies)
    else:
        running = False
        print("Goodbye!")