##  problem9  ##
def check(lists):
    for i in range(len(lists)-2):
        if lists[i]==1 and lists[i+1]==2 and lists[i+2]==3:
            return print('true')
        else:
            continue
    print('false')
list1=[1,1,2,3,1]
print("if the list1 is:")
print(list1)
check(list1)
list2=[1,1,2,4,1]
print("if the list2 is:")
print(list2)
check(list2)
list3=[1,1,2,1,2,3]
print("if the list3 is:")
print(list3)
check(list3)

