from collections import Counter
import re
import string
 
with open('alice_in_wonderland.txt') as f:
    text = f.read().lower()
 
# words = re.findall('\w+', text)
# top_10 = Counter(words).most_common(10)
# for word,count in top_10:
#     print(f'{word:<4} {"-->":^4} {count:>4}')


print(text.split()[500:700])


l = ([re.sub('[^a-zA-Z0-9]+', '', _) for _ in text.split()])


print("\n\n")

print(l[500:700])