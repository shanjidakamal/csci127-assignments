#examples from hackerrank that need to be tested
game_one_length = 7
game_one_colors = "RBY_YBR"
game_two_length = 6
game_two_colors = "X_Y__X"
game_three_length = 2
game_three_colors ="__"
game_four_length = 6
game_four_colors ="B_RRBR"
#function that should put all together
def Happy_Ladybugs(length, colors):
    return check_happiness(length, colors)
#checking ladybug happiness
def check_happiness(s,t):
    if happybug(s,t):
        return "YES"
    else:
        return "NO"
#sorting the values and characters [length/color]  
def sorting(t):
    characters= []
    values = []
    for item in t:
        if item != '_':
            if item not in characters:
                characters +=[item]
                values +=[1]
            else:
                 values[characters.index(item)] = values[characters.index(item)] + 1
    return values
#determining happiness
def happybug(s,t):
    if s < 3:
        if s == 0:
            return False
        elif s == 1 and t[0] == '_':
            return True
        elif s == 2 and t[0] == t[1]:
            return True
        else:
            return False
    else:
        values = sorting(t)
        if min(values) < 2:
            return False
    return True
print(Happy_Ladybugs(game_one_length,game_one_colors))
print(Happy_Ladybugs(game_two_length,game_two_colors))
print(Happy_Ladybugs(game_three_length,game_three_colors))
print(Happy_Ladybugs(game_four_length,game_four_colors))