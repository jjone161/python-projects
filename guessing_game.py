# Import the random module to generate random numbers
import random

lucky_number = random.randint(1, 24) # a random number between 1 and 24 is chosen

print("Let's play a game! Try to guess the magic number that I am thinking about!")


num_guesses = 0   # initiate a counter for the loop
user_guess = 0
while user_guess != lucky_number:       # while loop that keeps going until user guesses correctly
    user_guess = int(input("Please Pick a Number: "))
    num_guesses += 1

    if user_guess < lucky_number:       # Conditional statements to handle if the user guesses too low or too high
        print("Your guess is too low! Try again")
    elif user_guess > lucky_number:
        print("Your guess is too high! Try again")

print("That's the right number! You won!")
print(f"It took you {num_guesses} guesses to win the game!")

