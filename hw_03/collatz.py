def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 == 1:
            n = (3*n)+1
        count += 1
        print(n)
    
    return count

print ("count for 5: ", collatz(5))