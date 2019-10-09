
string = "ThiS is String  with Upper and lower case Letters"


def count_letters(s):

    s = string.lower()  
    s1 = s.split()
    s2 = "".join(s1)
    print(s2)


    letter_counts = {}

    for l in s2:
        letter_counts[l] = letter_counts.get(l ,0)+1


    _list = list(letter_counts.items())
    _list.sort()
    dic = dict(_list)
    

    for key,value in dic.items():
        print(key,"  ",value)


count_letters(string)