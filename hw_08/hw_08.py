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
def build_word_lists_by_index(words):
    d={}
    words=words.split()
    for i in range (0,len(words)-2):
        d.setdefault(words[i],[])
        d[words[i]].append(words[i+1])
    return d
#def build_words_lists(words):
#    d={}
#    words=words.split()
#    prev= words[0]
#    for nextword in words [1:]:
#        d.setdefualt(prev,[])
#        d[prev].append(nextword)
#        prev=nextword
#    return d

def build_words_lists(words):
    d={}
    words=words.split()
    first=words[0]
    second= words[1]
    for nextword in words[2:]:
        key=(first,second)
        d.setdefault(key,[])
        d[key].append(nextword)
        first = second
        second=nextword
    return d
import random
def gen_text(wl,number,tuple):
    first = tuple[0]
    second = tuple[1]
    text=[]
    for i in range(number):
        text.append(first)
        next=random.choice(wl[tuple])
        tuple=(second,next)
        first = second
        second = next
    return ''.join(text)
    

#f = open("moby-small.txt",encoding='utf-8')
#s = f.read()
#s="one two three four five six three seven three two three eight nine"
#d=build_word_counts(s)
#print(d)
#cleaned_string = clean_data(s)



f = open("moby-small.txt",encoding='utf-8')
s = f.read()
s=clean_data(s)
slist=s.split()
wl=build_words_lists(s)
print(gen_text(wl,100,(slist[0],slist[1])))
#print(s)
#words_uncleaned = build_word_counts(s)
#print(words_uncleaned)


#words = build_word_counts(cleaned_string)
#vals= words.values()
#vals= sorted(vals)   

#common_words=[]
#k=[]
#for k in words:
#    if words[k] > 1:
#       common_words.append([k,words[k]])
#following_words={}
#cleaned= cleaned_string.split()
#k = k
#for item in range(1,len(cleaned)-1):
#    if cleaned[item] in k:
#        dict = cleaned[item]
#        following_words.setdefault(dict,[])
#        following_words[dict].append(cleaned[item +1])

#print("Common Words Count : ",common_words)
#print("Following Words:",following_words)          