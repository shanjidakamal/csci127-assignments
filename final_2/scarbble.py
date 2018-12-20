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