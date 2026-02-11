# create a baby name rater 
# function for name rating logic
def rate_name(name):
    if len(name) < 3:
        return "Too short!"
    elif len(name) > 10:
        return "That's a mouthful!"
    elif name[0].lower() in "aeiou":
        return "Great name! Starts with a vowel - nice flow!"
    else:
        return "Great name!"
    

# ask user to input a baby name
baby_name = input("Enter a baby name: ")

# call the name rating function
print(rate_name(baby_name))