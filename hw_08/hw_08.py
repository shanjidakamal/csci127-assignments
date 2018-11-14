def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]= d[word] + 1
    return d

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result=result + letter.lower()
        elif letter in """./<,?!@#$%^&*()_=+""":
            result=result + ""
        else:
            result=result + " "
    return result

#s="one two three four five six three seven three two three eight nine"
#d=build_word_counts(s)
#print(d)
f = open("moby-small.txt",encoding='utf-8')
s = f.read()
cleaned_string = clean_data(s)
#print(s)
#words_uncleaned = build_word_counts(s)
#print(words_uncleaned)

words = build_word_counts(cleaned_string)
vals= words.values()
vals= sorted(vals)   

common_words=[]
k=[]
for k in words:
    if words[k] > 1:
       common_words.append([k,words[k]])

print("Common Words Count : ",common_words)

following_words={}
cleaned= cleaned_string.split()
k = k
for item in range(1,len(cleaned)-1):
    if cleaned[item] in k:
        dict = cleaned[item]
        following_words.setdefault(dict,[])
        following_words[dict].append(cleaned[item +1])
print("Following Words:",following_words)    
    
        