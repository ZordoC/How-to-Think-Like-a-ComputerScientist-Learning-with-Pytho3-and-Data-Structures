
class Point():

    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y 

    def reflect_x(self):
        """reflection of point on th x axis
        ie (3,5).reflect_x() is (3,-5)
        :returns: Point Object"""
        r_x = self.x
        r_y = self.y *-1

        return (Point(r_x,r_y))

    def __str__(self):
        return("The point is ({},{}) ".format(self.x,self.y))

    
    def slope_from_origin(self):
        """returns the slope of the line joining the origin to the point"""

        return (self.y / self.x)


    def get_line_to(self,target):
        """ Gives the output in format (m,b) of the line equation between two points
        :input(target): object class point
        :return: tuple 
        
        """

        m = (target.y - self.y) / (target.x - self.x)

        b = self.y - m * self.x

        return (m,b)


p1 = Point(3.023,5.12)

p2 = Point(2,1)



print(p1.get_line_to(p2))

# Fails if we call the same point
