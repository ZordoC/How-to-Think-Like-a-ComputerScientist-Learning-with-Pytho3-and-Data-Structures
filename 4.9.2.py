import turtle

def draw_square(animal, size):

    for _ in range(4):
        animal.forward(size)
        animal.left(90)
    
window = turtle.Screen()# Set up the window and its attributes

tess = turtle.Turtle()

#draw_square(tess,50)



def draw_growing_squares(animal,size,distance_apart):

    for j in range(5):

        draw_square(animal,size)
        
        animal.penup()
        x , y = animal.position()
        animal.goto(x + distance_apart / 2, y + distance_apart/2 )
        animal.pendown()

        size -=  distance_apart




draw_growing_squares(tess,50,30)

window.mainloop()
