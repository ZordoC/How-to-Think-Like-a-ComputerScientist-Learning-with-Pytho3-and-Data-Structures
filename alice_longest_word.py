from collections import Counter
import re
import string

with open('alice_in_wonderland.txt', 'r') as file:
    data = file.read().replace('\n', '')

 
words = re.findall('\w+', data)
top_10 = Counter(words).most_common(10)
for word,count in top_10:
    print(f'{word:<4} {"-->":^4} {count:>4}')



# data = data.lower()
# #l = re.sub("[^\w]", " ",  data) #re.sub(pattern, repl, string, count=0, flags=0)

# wordList = ([re.sub('[^a-z]+', '', _) for _ in data.split()])

# print(max(wordList,key = len))


# print(wordList)