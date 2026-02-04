# let's build a simple quiz game
# function to welcome user to the game

def game_welcome():
    user_name = input("Please enter name: ")
    print(f"Welcome {user_name} ! Let's play the game. Type 'quit' to close the game")
    return user_name

# call the function
user_name = game_welcome()

# create question bank
question_bank = ["How old is Jordan?", "Where was Jordan born?", "What is Jordan's favorite food?"]

# answers to quiz questions
quiz_answers = ["34", "Denver", "Pizza"]

# variable to increment and track score
user_score = 0

# loop to ask each question to user
for i, question in enumerate(question_bank):
    print(f"{i + 1}. {question}")
    # get user answers
    user_answer = input("Please enter answer: ")
    # conditional if user answers correctly
    if user_answer.lower() == quiz_answers[i].lower():
        print("Correct! Good Job!")
        user_score += 1
    # conditional if user wants to quit game
    elif user_answer == "quit":
        print("Closing game....goodbye!")
        break
    else:
        print("Wrong!")

if user_score == 3:
    print(f"Great job {user_name}! Your final score is {user_score}")
else:
    print(f"Nice try {user_name}! Try to get a better score soon!")
