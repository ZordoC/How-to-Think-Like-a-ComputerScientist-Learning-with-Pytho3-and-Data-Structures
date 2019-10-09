import turtle 

window =  turtle.Screen()
window.bgcolor('lightgreen')
window.title('2nd GUI')


alex = turtle.Turtle()
alex.speed(5)



l = [160, -43, 270, -97, -43, 200, -940, 17,-86]



for i in l:

    alex.forward(100)
    alex.right(i)


print("The drunken pirate is headed : {}".format(l[-1]))



