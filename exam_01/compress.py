def compress_word(w):
    word = w
    first_letter = word[:1]
    rest_word = word[1:]
    if word in "aeiou".find(word):
       print(first_letter + rest_word)
    else:
        print(first_letter + rest_word)
            
print(compress_word('apple'))

def sentence(line):
    line = 'I like to eat apple pie'
    line_one = line.split()
    return line_one
print(sentence(line_one))
    