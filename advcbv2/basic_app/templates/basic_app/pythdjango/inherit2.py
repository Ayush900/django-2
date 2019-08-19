class Animals():
    def __init__(self,type):
        self.type = type
    def c_eat(self):
        print("I eat meat...")
    def h_eat(self):
        print("I dont eat meat")
class birds(Animals):
    def __init__(self):
        pass

eagle=birds()
print('foe eagles:')
eagle.c_eat()
sparrow=birds()
print("for sparrow:")
sparrow.h_eat()
lion=Animals(type='carnivore')
print("for lion:")
print("I am a {}".format(lion.type))
lion.c_eat()
