def canMakeWord(letters,word):
    letters=list(letters)
    for i in word:
        if i in letters:
            letters.remove(i)
        else:
            return False
    return True
print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriin","eerie"))
print(canMakeWord("orrpgma","program"))
print(canMakeWord("orppgma","program"))

print("___________")
def withWild(letters,word):
    letters=list(letters)
    for i in word:
        if i in  letters:
            letters.remove(i)
        elif '?' in letters:
            letters.remove('?')
        else:
            return False
    return True
print(withWild("oo?m","mood"))
print(withWild("cava?ion","vacation"))