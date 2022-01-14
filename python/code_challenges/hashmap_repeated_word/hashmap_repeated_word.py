from collections import Counter
import string

def RepeatedWord(string):
    li = list(string.split(" "))
    repeated = Counter(li)
    for i in li:
      if(repeated[i] > 1):
        return i


string = "Once upon a time, finds the first word to occur more than Once in a string"
print(RepeatedWord(string))
