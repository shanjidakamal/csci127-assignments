def encode(w):
   l=[]
   d={}
   alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
   for item in w:
       if item in alpha:
           d.setdefault(item,0)
           d[item]=d[item]+1
   for keys,values in d.items():
       l1=[]
       l1.append(keys)
       l1.append(values)
       l.append(l1)
       
       return l
print(encode("abbaaacddaaa"))
