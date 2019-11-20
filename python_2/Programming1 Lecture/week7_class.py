# week7_class.py is a module
# within a module, we can have any number of classes

class Point:
    """
    Each class starts with the keyword of class
    Define a meaningful class name.
    class name convention: First letter capitalise
    eg: Point, Student, Car
    """
    def __init__(self, x=0, y=0):
        #x = 0 #local variable
        self.x = x # instance attribute/variable
        self.y = y
        print("Initialising ({}, {})".format(self.x, self.y))


point_a = Point(10, 12) # Instantiation, initialise a new object base on Point class
point_b = Point()