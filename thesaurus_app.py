#  Importing required libraries
import json
from difflib import get_close_matches

#  Converting json data into a python dictionary for easy access
dataset_dictionary = json.load(open("data/data.json", "r"))

#  Quick Check
# print(dataset_dictionary)
# print(dataset_dictionary['rain'])

#  Creating a function to find the word  thet user inputs and
#  return its meaning

def find_word(word):
    #  Converting the word to lower case for effective searching
    word = word.lower()

    #  Checking whether the word exist in the dataset
    if word in dataset_dictionary:
        return dataset_dictionary[word]

    #  checking for proper nouns
    elif word.capitalize() in dataset_dictionary:
        return dataset_dictionary[word.capitalize()]

    #  checking for acronyms
    elif word.upper() in dataset_dictionary:
        return dataset_dictionary[word.upper()]

    #  getting close matches of the user input  with the dataset
    elif len(get_close_matches(word, dataset_dictionary.keys())):
        choice = input(f"Do you mean {get_close_matches(word, dataset_dictionary.keys())[0]} ? Press Y/y for yes any other key for no: ")
        if choice == 'Y' or choice == 'y':
            return dataset_dictionary[get_close_matches(word, dataset_dictionary.keys())[0]]
        else:
            return "The word doesn't exist or cannot be processed. Please double check it."
    else:
        return "The word doesn't exist. Please double check it. "

#  main program
if __name__ == '__main__':
    word = input("Enter Word to search for : ")
    result = find_word(word)

    #  making the result more visible
    if type(result) == list:
        for item in result:
            print(item)
    else:
        print(result)