deck = "D S H C".split(' ')
rank = "2 3 4 5 6 7 8 9 10 J Q K A".split(' ')
d=[]
p1=[]
p2=[]
for i in range(len(deck)):
    for j in range(len(rank)):
        d.append(rank[j])
import random
random.shuffle(d)
for i in range(0,26):
    p1.append(d[i])
for j in range(26,52):
    p2.append(d[j])
class hand():
    def __init__(self,list):
        self.list = list
print(p1)
print(p2)

