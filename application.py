import json
from difflib import get_close_matches

data = json.load(open("data.json"))
 
def translate(myInput):  
    myInput = myInput.lower()
    
    if myInput in data:
        return data[myInput]

    elif myInput.title() in data:
        return data[myInput.title()]

    elif myInput.upper() in data: #in case user enters words like USA or NATO
        return data[myInput.upper()]

    elif len(get_close_matches(myInput, data.keys())) > 0:
        myOpenion = input(f"Did you mean {get_close_matches(myInput, data.keys())[0]} instead? Enter Y if yes, or N if no: ")
        
        if myOpenion == "Y":
            return data[get_close_matches(myInput, data.keys())[0]]
        
        elif myOpenion == "N":
            return "The word doesn't exist. Please double check it."
        
        else:
            return "We didn't understand your entry."
    
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
