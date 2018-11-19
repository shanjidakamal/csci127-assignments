def score(w):
    items=[]
    
    #one ='AEIOULNRST'
    #two='DG'
    #three='BCMP'
    #four='FHVWY'
    #five='K'
    #eight= 'JX'
    #ten= 'QZ'
    for letter in w:
        items.append(letter)
    score = 0
    for item in items:
        if item in 'AEIOULNRST':
            score += 1
        elif item in 'DG':
            score += 2 
        elif item in 'BCMP':
            score += 3 
        elif item in 'FHVWY':
            score += 4 
        elif item in 'K':
            score += 5 
        elif item in 'JX':
            score +=8 
        elif item in 'QZ':
            score += 10 
    return score
print(score('HELLO'))