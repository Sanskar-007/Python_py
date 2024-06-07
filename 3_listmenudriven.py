"""
3. Write a menu driven program to practice List functions. Validate input data wherever
required.
Display following menu:
1. Accept Data
    a) add at last position
    b) add at given position
2. Delete data by value 
    display message 
    deleted successfully
    or not found
3. delete data by position
    a) delete last element
    b) delete from particular position
4. sort
    a) ascending
    b) descending
5. reverse

6. Print in sorted order without changing original list

7. print in reverse order without changing original list

8. display data

    a) normal
    
    b) numbered
    
"""
lst=[1,8,4,2,4,7,3,6,5]
def modifyList(n,m):
    if n<=len(lst) and n>=0:
        if n==len(lst):
            lst.append(m)
        else:
            lst.insert(n,m)
        return 1
    else:
        return -1
    
def deleteByValue(n):
    if n in lst:
        ans=input("do you want to delete the value(y/n): ")
        if ans=='y':
            while n in lst:
                lst.remove(n)
            return 1
        elif ans=='n':
            return 2
        else:
            return 3
    else:
        return -1

def deleteByPos(n):
    if n<len(lst) and n>=0:
        lst.pop(n)
        return 1
    else:
        return -1

    
    
    
    



choice=0
while choice!=9:
    choice=int(input("""
                     1. Accept Data
                     2. Delete data by value
                     3. Delete data by postion
                     4. Sort
                     5. Reverse 
                     6. Print in sorted order without changing the original list
                     7. Print in reverse order without chnaging the original list
                     8. Display data
                     9. Exit
                     Enter your choice here: """))
    match choice:
        case 1:
            ch=input("""
                a) add at last position
                b) add at given position
               """)
            s=0
            if ch=="a":
                m=int(input("""
                Please enter the element to add to last position of the list: """))
                s=modifyList(len(lst), m)
            elif ch=="b":
                n=int(input("""
                Please enter postion to add element(starts from 0): """))
                m=int(input("""
                Please enter element to add to the list: """))
                s=modifyList(n, m)
            else:
                print("wrong choice")
            if s==1:
                print(lst)
            if s==-1:
                print("index out of range")
        case 2:
            n=int(input("Enter value you want to delete from the list"))
            s=deleteByValue(n)
            if s==1:
                print("Deleted successfully")
                print(lst)
            elif s==2:
                print("found but not deleted")
            elif s==3:
                print("wrong choice")
            else:
                print("element not found")
                
        case 3:
            n=int(input("enter the postion to delete(starts from 0): "))
            s=deleteByPos(n)
            if s==1:
                print(f"value at position {n} deleted")
                print(lst)
            else:
                print("position out of range")
                
        case 4:
            ch=input("""
                     a) ascending
                     b) descending
                      enter here: """)
            if ch=="a":
                lst.sort()
            elif ch=="b":
                lst.sort(reverse=True)
            else:
                print("wrong choice")
        case 5:
            lst.reverse()
            print(lst)
        case 6:
            slst=sorted(lst)
            print(slst)
        case 7:
            revlst=list(reversed(lst))
            print(revlst)
        case 8:
            print(lst)
        case 9:
            print("thank you for trying our program")
        case _:
            print("please enter a valid choice ")
        
    
