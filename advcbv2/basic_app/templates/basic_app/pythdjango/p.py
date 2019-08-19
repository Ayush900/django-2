class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height
class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return Circle.pi*self.radius*self.radius
    def circumference(self):
        return 2*Circle.pi*self.radius
class
c1 = Circle(20)
print('The area of circle c1 is {} and its circumference is {}...'.format(c1.area(),c1.circumference()))