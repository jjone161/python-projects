# Build a magic 8 ball that answers yes/no questions randomly
import random

answers = ["yes", "no", "maybe", "kinda", "definitely"]


magic = True  # game continues while magic is true

while magic == True:
    user_question = input("Please ask a question: ")
    #conditional for if user quits the game
    if user_question == "quit":
        magic = False
        print("Goodbye!")
    else:
        print(random.choice(answers))
    
    
    

