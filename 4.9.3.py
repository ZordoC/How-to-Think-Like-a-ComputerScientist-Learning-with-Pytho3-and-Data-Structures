import turtle 

window =  turtle.Screen()
window.bgcolor('lightgreen')
window.title('Hexagon')

alex = turtle.Turtle()
alex.speed(1)
alex.color("pink")
alex.pensize(10)

def draw_poly(t,n,sz):

    for i in range(n):

        t.forward(sz)
        t.right(45)


draw_poly(alex,8,50)

window.mainloop()