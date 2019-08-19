class triangle():

    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
b = int(input("Enter the base of the triangle:"))
h = int(input("Enter the height of the triangle:"))
t1 = triangle(b,h)
print("The area of the triangle is : {}".format(t1.area()))
