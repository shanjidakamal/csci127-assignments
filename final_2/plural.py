
def countPlurals(line):
    seper=line.split()
    value=0
    for i in seper:
        if i[len(i)-1] == "s":
            value += 1
    return value

print(countPlurals("dogs love to eat dogbones"))
print(countPlurals("cars bikes trains buses taxi"))

def notPossesive(line):
    seper=line.split()
    value=0
    for i in seper:
        if i[-1]== "s" and i[-2]!= "'": ## -2 so it looks for the apostrephe to the s at the end
            value += 1
    return value
print(notPossesive("dog's cat's birds rats hamsters"))
