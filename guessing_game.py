# Import the random module to generate random numbers
import random

# Function for user guess
def get_guess():
    return int(input("Please Pick a Number: "))

# function to check if guess is too high/too low
def check_guess(guess, secret):
    if guess < secret:       # Conditional statements to handle if the user guesses too low or too high
        print("Your guess is too low! Try again")
        return False     # wrong guess
    elif guess > secret:
        print("Your guess is too high! Try again")
        return False   # wrong guess
    else:
        return True    # correct guess!


lucky_number = random.randint(1, 24) # a random number between 1 and 24 is chosen

print("Let's play a game! Try to guess the magic number that I am thinking about!")

num_guesses = 0   # initiate a counter for the loop
guess = 0
while guess != lucky_number:       # while loop that keeps going until user guesses correctly
    guess = get_guess()            # Get a number from the user
    check_guess(guess, lucky_number)
    num_guesses += 1

print("That's the right number! You won!")
print(f"It took you {num_guesses} guesses to win the game!")

