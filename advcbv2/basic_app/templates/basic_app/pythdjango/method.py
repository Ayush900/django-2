class square():
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth
    def area(self):
        return self.length * self.bredth
    def perimeter(self):
        return 2 * (self.length+self.bredth)

sq1 = square(15,10)
sq2 = square(10,10)
print("The first square is of length = {} and bredth = {}".format(sq1.length,sq1.bredth))
print("The area of first square is {} and the perimeter is {}".format(sq1.area(),sq1.perimeter()))
print("The second square is of length = {} and bredth = {}".format(sq2.length,sq2.bredth))
print("The area of second square is {} and the perimeter is {}".format(sq2.area(),sq2.perimeter()))
