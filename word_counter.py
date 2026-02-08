# building a quick word counter 

# start with empty dictionary to add words to
websters = {}


# ask the user for a 5 word sentence
sentence = input("Enter a 5 word sentence: ")

# split the sentence into a list of words
split_sentence = sentence.split()

# loop through each word
for word in split_sentence:
    if word.lower() in websters:
        websters[word.lower()] += 1
    else:
        websters[word.lower()] = 1
        
        
print(websters)
    
        
    
        
