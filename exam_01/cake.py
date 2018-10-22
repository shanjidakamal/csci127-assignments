
def division_cake(A,B,u):
   unit = A/B
   people_invited = u / unit
   return people_invited

print(int(division_cake(5,10,1)))
print(int(division_cake(20,40,1)))
print(int(division_cake(60,6,10)))
