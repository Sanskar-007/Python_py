"""
1.  Write a menu driven program to practice String functions
    Design following menu
    a. display characters from even position
    b. display characters from odd position
    c. display length of a string
    d. add a at the end of string length times
    e. exit

"""
s="this is a demo string"
#s="gamerlife"
def displayEvenChar(st):
    return s[1:len(s):2]
    
def displayOddChar(st):
    return s[0:len(s):2]
    
def adda(st):
    for i in st:
        st=st+"a"
    return st
   
    
choice = ""
while choice != "e":
    choice = input("""
    a. display characters from even position
    b. display characters from odd position
    c. display length of a string
    d. add a at the end of string length times
    e. exit
    Enter your choice here(a,b,c,d,e): """)
    
    
    match choice:
        case 'a':
            print("\n",displayEvenChar(s))
            
        
        case 'b':
            print("\n",displayOddChar(s))
            
        
        case 'c':
            print(f"\n   the length of the given string ({s}) is",len(s))
        
        case 'd':
            ss=adda(s)
            print(ss)
        
        case 'e':
            print("\n    thank you for trying out this programme")
        
        case _:
            print("\n   wrong choice")
    
    
    
    