import turtle 

window =  turtle.Screen()
window.bgcolor('lightgreen')
window.title('2nd GUI')


alex = turtle.Turtle()
alex.speed(1)


#An equilateral triangle

for i in range(3):

    alex.forward(100)
    alex.left(120)
    


#A square

alex.color("red")

for i in range(4):

    alex.forward(100)
    alex.left(90)

#A hexagon (six sides)

alex.color("yellow")

for i in range(6):

    alex.forward(100)
    alex.right(60)



#An octagon (eight sides)


alex.color("blue")

for i in range(8):

    alex.forward(100)
    alex.left(45)