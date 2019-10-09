def replace(s,old,new):
    '''''
    replace all occurences of old with new in a string s, works for one letter
    
    :input(s):string
    :input(old):string
    :input(new):string
    :output(string): string
    '''''

    string = " ".join(s)
    string = string.split()


    for i,k in enumerate(string):
        if k == old:
            string[i] = new
    

    string = ' '.join(string)

    return string



def myReplace(s,old,new):
    '''''
    replace all occurences of old with new in a string s, works for multiple letters
    
    :input(s):string
    :input(old):string
    :input(new):string
    :output(string): string
    '''''
    return new.join(s.split(old))


print(myReplace("Hello","ll","OO"))

print(myReplace("MIssIssIppI",'I','i'))

song = "I love spom! Spom is my favorite food. Spom, spom, yum!"

print("\n")

print(myReplace(song, "om", "am"))

print("\n")

print(myReplace(song, "o", "a"))
