
def reverse_string(string):
    '''''
    Prints a reversed string using the in built reversed function
    :input: string 
    '''''
    for s in reversed(string):
        print(s,end = "")


     
reverse_string("happy")

print("\n")

def reversed_string_slicin(string): 
    '''''
    Reverses a string and returns it using slicing
    :input: string 
    '''''
    return string[::-1]


happy =  reversed_string_slicin("happy")

print(happy)








