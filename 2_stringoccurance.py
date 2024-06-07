"""

2. Write a program to accept a string from user.
Accept a second string from user to search and find all occurrences of in the given string.
e.g
s1=This is string
check=is
is-2
is-5
count=2

s1=”this is cat and cat is cute, where is your cat?”
check=cat
cat-8
cat-16
cat-43
count=3

"""

def findallocc(s1,s2):
    pos=s1.find(s2)
    count=0
    while pos!=-1:
        print(f"{s2}-{pos}")
        pos=s1.find(s2,pos+1)
        count +=1
    print(f"count={count}")
    
    
s1= input("please enter a string : ")
s2= input("enter another that to locate in the previous string : ")
findallocc(s1,s2)