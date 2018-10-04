import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l
l = build_random_list(10,50)
print(l)

#Write and test a function named locate(l,value)
def locate(l,value):
    i=0
    while i < len(l):
        if l[i] == value:
            return i 
        else:
            i += 1
    return -1
print(locate(build_random_list(10,50),50))

#Write and test a function named count(l,value)
def count(l,value):
    count=0
    for value in l:
        if(value == 50):
            count = count + 1
    return count
print(count(build_random_list(10,50),50))

#Write and test a function named reverse(l)
def reverse(l):
    l = build_random_list(10,50)
    print(l)
    return l[ : :-1]
print(reverse(l))
    
#Write and test a function named is Increasing(l)
def isincreasing(l):
    for i in range(len(l) - 1):
        if l[i] > l [i + 1]:
            return False
    return True
print(isincreasing(build_random_list(10,50)))
    
#Write and test a function named palindrome(l)
def palindrome(l):
    l = build_random_list(10,50)
    if l == l[ : :-1]:
        return True
    else:
        return False
print(palindrome(build_random_list(10,50)))