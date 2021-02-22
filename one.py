#importing a json file
import json
from difflib import get_close_matches

data= json.load(open("data.json"))

#defining a function that returns values i.e [] from the json file(dict)

def translate(word):                         # we can use any other variable like w in function
    word=word.lower()                        # word.lower()to make  it suitable for capital letters
    if word in data:                            
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input( "Did you mean %s instead? Press Y or N" % get_close_matches(word,data.keys())[0])      #elif to get best match,[0] for closest match,take y or n as input
        if yn=="Y":
            return data[ get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "Doesn't exist"
        else:
            return "Didn't understand you!!"
    else:                                   
        return "Doesn't exist"
    

word= input("Enter the word:")
output= translate(word)

if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)