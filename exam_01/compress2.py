#code doesnt work
def compress_word(w):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']
    new_word = []
    for i in w:
        if i not in vowels:
            new_word.append(i)
    new = ''.join(new_word)
    return new       
        
            
print(compress_word('apple'))
print(compress_word('special'))

#def sentence(line):
 #   line = 'I like to eat apple pie'
#   line_one = line.split()
 #   return line_one
#print(sentence(line_one))
    
#code doesnt work