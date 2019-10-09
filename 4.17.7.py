def to_secs(h,m,s):
    '''''
    converts %h %m %s to seconds

    :input: int 
    :output: int
    '''''

    hours = (h)*3600
    mins = (m)*60
    return( int(hours + mins + s)) 
    


print(to_secs(2,30,10))
print(to_secs(2,0,0))
print(to_secs(0,2,0))
print(to_secs(0,-10,10))

print(to_secs(2.5,0,10))
