import json
import os
from difflib import get_close_matches
 
 
data= json.load(open("data.json"))
 
def def_finder(word):
    if word in data:
        return data[word]
 
    elif word.lower() in data:
        return data[word.lower()]
 
    elif word.upper() in data:
        return data[word.upper()]
 
    elif word.title() in data:
        return data[word.title()]
    
    elif word not in data:
         matches= get_close_matches(word,possibilities=data.keys(), cutoff= 0.8)
         if len(matches)>0:
             yn= input(f"Did you mean '{matches[0]}' instead of '{word}', press 'y' if yes and 'n' if not: ")
             if yn== "y" or yn== "Y":
                 return data[matches[0]]
             else:
                 return (f"The word '{word}' doesn't exist. Please re-check!") 
    
         else:
             return (f"The word '{word}' doesn't exist. Please re-check!")

 
input_word = input("Enter a word to find the definition: ")
 
definitions= def_finder(input_word)
 
 
if type(definitions)== list and len(definitions)>1:
    for i,val in enumerate(definitions, start=1):
         print(f"Definition {i}: { val}")
 
elif type(definitions)== list and len(definitions)== 1:
    print("Definition: "+definitions[0])
 
else:
    print(definitions)