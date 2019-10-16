
class Point():

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y 

 

p1 = Point(1,2)

p2 = Point(4,10)



def distance(p1,p2):
    
    """ Compute distance between two objects
        :input(p1): point class object
        :input(p2): point class object
    
    """
    return ((p2.x - p1.x)*2 + (p2.y - p1.y))**0.5


print(distance(p1,p2))