
def count_letters(string,letter):
    ''''' 
    Count a given letter in a specified string
    
    :input(string): string 
    :input(letter): string
    :return(count): int

    ''''' 
    count = 0

    for let in string:

        if let == letter:
            count += 1

    return count 

print(count_letters("banana","a"))


