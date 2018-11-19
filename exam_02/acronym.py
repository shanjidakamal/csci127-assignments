def makeacronym(w):
    acronym=[]
    each_word= w.split(' ')
    for word in each_word:
         acronym.append(word[0])
    return ''.join(acronym)

print(makeacronym('LAUGH OUT LOUD'))
print(makeacronym('Read the fine manual'))
print(makeacronym('In my humble opinion'))
print(makeacronym('In my not so humble opinion'))