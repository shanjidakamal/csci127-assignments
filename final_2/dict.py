def addLine(d,line):
    line=line.lower()
    for item in line.split():
        if item[0] not in d:
            d[item[0]]=[item]
        elif item not in d[item[0]]:
            d[item[0]].append(item)
    return d
d = {"c": ["cat", "cookies"],"m": ["milk"],"s": ["scared"], "d":["dog"]} #define the d dictionary so addline function knows how to create the dictionary
addLine(d, "Santa went down the chimney")
addLine(d, "He ate some cookies and milk")
addLine(d, "He also scared the cat and the dog as he put the presents down")
addLine(d, "As the children came down the stairs, Santa said HOHO and quickly went up the chimney")
print(d)

print("______________ added more words")#just checking the process 
addLine(d, "Children were ecstatic when they all opened their presents")
print(d)

def spellcheck(d,word):
    word=word.lower()
    if word[0] in d:
        if word in d[word[0]]:
            return True
    return False
print("__________") #divide the two parts printing
print(spellcheck(d, "chimney")) #True
print(spellcheck(d, "chimnay")) #False
print(spellcheck(d, "reindeer")) #False
print(spellcheck(d, "sacred")) #False
print(spellcheck(d, "cookies")) #True