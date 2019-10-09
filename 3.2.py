def which_day(start, nights):
    days = ['Monday', 'Tuesday', 'Wednesday', 
            'Thursday', 'Friday', 'Saturday',"Sunday"]
    
    return days[(start + nights) % 7]

print(which_day(1, 10))  # Friday 

