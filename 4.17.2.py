


def day_name(num):
    '''''
    Converts integer number ( 0 - 6) into a day of the week
    :input: int
    :output: string
    '''''
    l = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


    if num >= 0 and num <=6:

        return(l[num])

    else:

        return None 


print(day_name(3))

print(day_name(10))
