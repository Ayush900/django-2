#class keyword is used to create your own classes in python ,just like the sets,lists,tuples etc. .these classes are also known as objects and this type of programming involving the creation of your own classes or objects is known as object oriented programming or oops....#
class football_team:               #Here the new object created is the football_team which contain an attribute which tells about the league of the football team #
    def __init__(self,league,pos):
        self.league=league
        self.pos=pos


arsenal=football_team(league = 'bpl',pos=4)
barca=football_team(league = 'la_liga',pos=1)

print('Arsenal play in {} and its position in league is {}'.format(arsenal.league,arsenal.pos))
print('FC Barcelona play in {} and its position in league is {}'.format(barca.league,barca.pos))