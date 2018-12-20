def addLine(d,line):
    line=line.lower()
    for item in line.split():
        if item[0] not in d:
            d[item[0]]=[item]
        elif item not in d[item[0]]:
            d[item[0]].append(item)
    return d
d = {"c": ["cat", "cookies"],"m": ["milk"],"s": ["scared"]}
addLine(d, "Santa went down the chimney")
addLine(d, "He ate some cookies and milk")
addLine(d, "He also scared the cat and the dog as he put the presents down")
print(d)


