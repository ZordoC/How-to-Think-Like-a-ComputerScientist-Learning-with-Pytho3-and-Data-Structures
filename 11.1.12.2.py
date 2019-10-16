
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
        return("The point is {} , {} ".format(self.x,self.y))

    
    def slope_from_origin(self):
        """returns the slope of the line joining the origin to the point"""



p1 = Point(3,5)


print(p1)

p1_r = p1.reflect_x()

print(p1_r)
