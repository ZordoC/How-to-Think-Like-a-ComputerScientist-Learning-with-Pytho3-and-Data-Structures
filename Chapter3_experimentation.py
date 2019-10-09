import turtle 

window =  turtle.Screen()
window.bgcolor('lightgreen')
window.title('2nd GUI')


alex = turtle.Turtle()

alex.color("hotpink")

alex.speed(1)

for i in range(4):

    alex.forward(50)
    alex.left(90)


colors = ["yellow", "red", "purple", "blue"]

for color in colors:
    alex.color(color)
    alex.forward(50)
    alex.left(90)




alex.shape("turtle")

alex.penup()
alex.forward(100)
alex.pendown()


alex.penup()
size=20

for _ in range(30):

    alex.stamp()
    size = size + 3
    alex.forward(size)
    alex.right(24)

alex.color('green')

window.mainloop()


n=1027371 

while n != 1:
    print(n,end=", ")
    if n % 2 == 0:
        n = n //2 
    
    else:
        n = n * 3 + 1


print(n, end= ".\n")

