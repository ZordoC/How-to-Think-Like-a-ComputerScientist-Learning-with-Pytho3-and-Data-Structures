
def is_even(num):

    if num % 2 == 0:
        return(True)
    else:
        return False


def is_odd(num):

    if is_even(num) == True:
        return False
        
    else: 
        return True 



print(is_even(2))
print(is_even(3))
print(is_even(4))
print(is_even(5))
print(is_even(102398323))

print(is_odd(2))
print(is_odd(3))
print(is_odd(4))
print(is_odd(5))
print(is_odd(102398323))


