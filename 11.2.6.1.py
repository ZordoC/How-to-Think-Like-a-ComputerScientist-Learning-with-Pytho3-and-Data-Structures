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

class Rectangle:

    def __init__(self,posn,w,h):
        self.corner = posn
        self.width = w 
        self.height = h
    

    def __str__(self):
        return "({0}, width = {1}, height = {2})".format(self.corner,self.width,self.height)


    def area(self):
        return self.width * self.height


    def perimeter(self):
        return self.width * 2 + self.height *2 

    def flip(self):
        self.width , self.height =  self.height , self.width

    
    def contain(self,point):
        if point.y >= 0 and point.x >=  0:


            if  point.y < self.height and point.x < self. width:
                return True
        
            else: 
                return False
        else:
            return False



r =  Rectangle(Point(0,0),10,5)

# testing 

assert (r.area() == 50),"Should be 50" 
assert(r.perimeter() == 30), "Should be 30 "



r = Rectangle(Point(100, 50), 10, 5) 

assert (r.width == 10 and r.height == 5)
 
r.flip()

assert (r.height == 10 and r.width == 5)

r.flip()

assert( r.contain(Point(0,0)) == True )
assert( r.contain(Point(3,3)) == True )
assert( r.contain(Point(3,7)) == False )
assert( r.contain(Point(0,0)) == True )
assert( r.contain(Point(3,4.99999)) == True )
assert( r.contain(Point(-3,-3)) == False )


def intersects(self, other):
    return not (self.height.x < other.bottom_left.x 
    or self.bottom_left.x > other.top_right.x 
    or self.top_right.y < other.bottom_left.y 
    or self.bottom_left.y > other.top_right.y)


