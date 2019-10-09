import turtle 

window =  turtle.Screen()
window.bgcolor('lightgreen')
window.title('2nd GUI')


alex = turtle.Turtle()

alex.speed(1)


l = [(160, 20), (-43, 10), (270, 8), (-43, 12)]



for i,j in l:

    alex.forward(i)
    alex.right(j)


window.mainloop()