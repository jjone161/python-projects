# import random module to generate numbers at random
import random

# pick a random number between 1 and 23
lucky_number = random.randint(1, 23)

num_guesses = 0
user_guess = 0

# create a function for the user to guess a numnber
def get_guess():
   return (int(input("Please select a number: ")))

# create a function for whether a guess is high, low, or correct
def check_guess(guess, secret):
   if guess < secret:
      print("Number is too low! Try again! ")
      return False
   elif guess > secret:
      print("Number is too high! Try again! ")
      return False
   else:
      print("You chose the correct number! Congrats!")
      print(f" you won the game in {num_guesses} guesses")
      return True
# While look to continue the game until user wins
while user_guess != lucky_number:
   user_guess = get_guess()
   check_guess(user_guess, lucky_number)
   num_guesses += 1



      
   