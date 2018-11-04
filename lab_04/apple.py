#sample numbers used on hackerrank
s, t = 7, 11
a, b = 5, 15
apples = [-2, 2, 1]
oranges = [5, -6]


def countApplesAndOranges(s, t, a, b, apples, oranges):
    s_apples = 0
    s_oranges = 0
    for item in apples:
        apple_loc = (a + item)
        if apple_loc in range(s, t + 1):
            s_apples= s_apples + 1
    for item in oranges:
        orange_loc = (b - item)
        if orange_loc in range(s, t + 1):
            s_oranges= s_oranges + 1           
    return str(s_apples) + "\n" + str(s_oranges)

print(countApplesAndOranges(s, t, a, b, apples, oranges))