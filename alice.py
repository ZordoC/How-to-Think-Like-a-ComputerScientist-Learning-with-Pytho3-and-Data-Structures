import string
import re


with open('alice_in_wonderland.txt', 'r') as file:
    data = file.read().replace('\n', '')

def remove_punctation(phrase):
    text_sans_punct = ""

    for letter in phrase:
        if letter not in string.punctuation:
            text_sans_punct += letter
        
    return text_sans_punct

#data.translate(str.maketrans('', '', string.punctuation))

data = data.lower()
#l = re.sub("[^\w]", " ",  data) #re.sub(pattern, repl, string, count=0, flags=0)

wordList = ([re.sub('[^a-z]+', '', _) for _ in data.split()])


print(wordList)

#print(wordsList)

wordcount = {}

for word in wordList:
    
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

word_count_l = list(wordcount.items())

# word_count_l.sort()

# word_count =  dict(word_count_l)


print(wordcount)

# for key,value in word_count.items():

#     print ( value, ":" , key ) 


