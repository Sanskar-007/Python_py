import re
s='Something is there somewhere'
m=re.search("s.*e",s,re.I)
if m!=None:
    print("found")
    print(m.group())
    print(m.span())
else:
    print("Not found")

s='Something is there somewhere'
m=re.search("s.*?e",s,re.I)
if m!=None:
    print("found")
    print(m.group())
    print(m.span())
else:
    print("Not found")

s='Something is there somewhere'
m=re.search("t.*?e",s,re.I)
if m!=None:
    print("found")
    print(m.group())
    print(m.span())
else:
    print("Not found")

#match always checks the patern at the begining of the line
m=re.match("t.*?e",s,re.I)
if m!=None:
    print("found")
    print(m.group())
    print(m.span())
else:
    print("Not found")


lst=re.findall("s.*?e",s,re.I)
if lst!=None:
    print(lst)
else:
    print("Not found")


lst=re.finditer("s.*?e",s,re.I)
if lst!=None:
    for m in lst:
        print(m.group())
        print(m.span())
else:
    print("Not found")

#it helps to create regexp object to store regular
# expression and flags in it
    
myreg=re.compile("s.*?e",re.I)
m=myreg.search(s)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("Not found")














    
