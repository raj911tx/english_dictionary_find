import json
from difflib import get_close_matches

file=open("data.json")
data=json.load(file)

def load_data(word):   
    match=get_close_matches(word,data.keys(),cutoff=0.8)[0]
    if word in data:         
        meaning=data[word]
        print("{}:".format(word))
        for i in range(len(meaning)):
            print("{}".format(meaning[i]))
    elif word.title() in data:
        return load_data(word.title())
    elif word.upper() in data:
        return load_data(word.upper())
    elif len(match)>0:
        conf = input("Did u mean {}? Enter Y for yes and N for no:\n".format(match))   
        if conf=='Y':
            return load_data(match)
        else:
            return ("Try again")
    else:
        return "The word doesnt exist"

word=input("Enter Word: ").lower()
load_data(word)