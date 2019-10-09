import turtle 

window =  turtle.Screen()
window.bgcolor('lightgreen')
window.title('2nd GUI')


alex = turtle.Turtle()


alex.penup()

for _ in range(12):

    alex.forward(100)
    alex.stamp()
    alex.backward(100)
    alex.right(30)

alex.color('green')


