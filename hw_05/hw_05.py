'''Write a function filterodd(l) that takes in a list and returns a new
list that consists of only the odd numbers from the original list. That
is the list [1,2,3,4,5,6,7,8] would return a new list [1,3,5,7]. The
lists don't have to be in order.'''

l=[1,2,3,4,5,6,7,8,9,10,11,12]

def filterodd(l):
    newlist=[]
    for n in l:
        if n % 2 == 1:
            newlist.append(n)
    return newlist
print(filterodd(l))

'''Write a function mapsquare(l) that takes a list and returns a new
list that consists of the original items squared. For example, the list
[4,2,5,3,5] would return a new list [16,4,25,15,25]'''

l2=[12,3,5,6,2,1,8,9,0,14,7]
def mapsquare(l2):
    newlist2=[]
    for n in l2:
        newlist2.append(n ** 2)
    return newlist2
print(mapsquare(l2))
            
            



