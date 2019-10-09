
week_dayz = {"0":"Monday","1":"Tuesday","2":"Wednesday","3":"Thursday","4":"Friday","5":"Saturday","6":"Sunday"}


user = input("What is the number of the day ?\n")

for key in week_dayz:

    if key == user:
        print(week_dayz[key])
   