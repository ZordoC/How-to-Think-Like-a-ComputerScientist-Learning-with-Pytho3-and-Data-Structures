import turtle 

window =  turtle.Screen()
window.bgcolor('lightgreen')
window.title('2nd GUI')


alex = turtle.Turtle()
alex.speed(3)

def make_star(animal,length):

    for k in range(6):

        animal.forward(length)
        animal.right(144)



#make_star(alex,100)



def move_stars(animal):

    for _ in range(5):
        make_star(animal,100)
        animal.penup()
        animal.forward(250)
        animal.right(144)
        animal.pendown()
        
move_stars(alex)
