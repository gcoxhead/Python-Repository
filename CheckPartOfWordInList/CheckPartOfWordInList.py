
# import regular expression module
import re

# Create a list of words
inputs = ["dog", "cat", "car", "boat", "keyboard", "care","caretaker", "persistance", "badger", "parsnip", "sofa", "horn", "cooking"]

#Create empty list
matchWords = []
#define a search pattern, use '.' to include any character
pattern = "c."

#define the function and pass pattern and inputs list as arguments
def check_words(pattern, inputs):

    # print console message
    print("\n**** Checking words ****\n")
    print("Words that contain "+ pattern +"\n")
    match_count = 0
    word_count = 0

    #loop through words in the input list
    for item in inputs:

        # increase word count for each word
        word_count +=1

        #use findall method to create match object
        match = re.findall(pattern,item)

        #if a match is found, print word, increase match_count. append list
        if match:
            match_count +=1
            matchWords.append(item) 
            print (item)

    #convert count integers to strings
    match_count = str(match_count)
    word_count = str(word_count)

    # create message object and print
    message = "\n" + match_count + " matches found out of " + word_count +" words.\n"
    print(message)
    print(matchWords)

#call the check_words method
check_words(pattern, inputs)
