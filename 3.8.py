

def check_right(a,b,c):

    threshold = 1e-7

    if abs((a**2 + b**2) - c**2) < threshold:

        print("Triangle is right indeed")
    
    else: 
        print("Triangle is not right brah")



def extended_check_right(a,b,c):

    if a>=b and a>=c:
        h = a
    elif b>=a and b>=c:
        h = b
    elif c>=a  and c>=b:
        h = c
    
    threshold = 1e-7

    if abs((a**2 + b**2) - h**2) < threshold:
        
        print("Triangle is right")

    else:
        print("Triangle is not right")



extended_check_right(1,1,1)