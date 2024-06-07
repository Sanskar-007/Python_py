from BankAccount import *

#example list to check funtions
lst=[Savingacc("abc",1111,10000,50),
     Currentacc("abdc",2222,20000,500),
     Dematacc("xyz",3333,1000000,5),
     Savingacc("manu",1234,100000,20000)]

sminbal=2000        #minimum balance for savings account
cminbal=10000       #minimum balance for savings account
dminbal=50000       #minimum balance for savings account

#______________________________________________________________________________
 
#funtion to add new account and diplay id if created successfully
def addnewAccount(ch):
    s=None
    name=input("Enter the name: ")
    pin=int(input("Enter the pin : "))
    bal=int(input("Enter the balance: "))
    if ch=='a':               #checking the type of account
        if bal>=sminbal:      #checking if opening balance>= minimum balance
            ecs=int(input("Enter the ECS amount: "))
            s=Savingacc(name,pin,bal,ecs)
            lst.append(s)
            print("Account successfully created")
            print("this is your id:",lst[len(lst)-1].get_aid())
        else :
            print("insufficient amount, less than minimum balance")
    elif ch=="b":            #checking the type of account
        if bal>=cminbal:     #checking if opening balance>= minimum balance
            ntr=int(input("Enter the No. of Transaction: "))
            s=Currentacc(name,pin,bal,ntr)
            lst.append(s)
            print("Account successfully created")
            print("this is your id:",lst[len(lst)-1].get_aid())
        else:
            print("insufficient amount, less than minimum balance")
            
    elif ch=="c":             #checking the type of account
        if bal>=dminbal:      #checking if opening balance>= minimum balance
            com=int(input("Enter the Commission: "))
            s=Dematacc(name,pin,bal,com)
            lst.append(s)
            print("Account successfully created")
            print("this is your id:",lst[len(lst)-1].get_aid())
        else:
            print("insufficient amount, less than minimum balance")
    else:
        print("wrong choice")
    #if s!=None:
        #lst.append(s)

#Function to withdraw amount from the account
def withdraw(i,pin):
    #i=input("Enter your id: ")
    #pin=int(input("Please enter the PIN: "))
    #iterate through list using for loop to get the required object
    for ind,ob in enumerate(lst):
        if ob.get_aid()==i and ob.get_pin()==pin: #to authenticate id and pin
            ob.withdraw()
            return 1
#        else:
 #2           continue
    return -1
        
def deposit(i,pin):
    
    #iterate through list using for loop to get the required object
    for ind,ob in enumerate(lst):
        if ob.get_aid()==i and ob.get_pin()==pin: #to authenticate id and pin
            ob.deposit()
            return 1
        else:
            continue
    return -1
    
def changePin(i,pin,newpin):
    
    #iterate through list using for loop to get the required object
    for ind,ob in enumerate(lst):
        if ob.get_aid()==i and ob.get_pin()==pin: #to authenticate id and pin
            ob.set_pin(newpin)
            print("Pin changed successfully")
            return 1
        else:
            continue
    return -1
    
def checkBalance(i):
    
    #iterate through list using for loop to get the required object
    for ind,ob in enumerate(lst):
        if ob.get_aid()==i: #to check if id exist
            print(ob.get_balance())
            return 1
        else:
            continue
    return -1
def closeAcc(i,pin):
    
    #iterate through list using for loop to get the required object
    for ind,ob in enumerate(lst):
        if ob.get_aid()==i and ob.get_pin()==pin: #to authenticate id and pin
            ans=input("do you want to close the account?(y/n)")
            if ans=='y':
                lst.pop(ind)
                print("Account closed successfully")
                #ob=None
                return 1
            elif ans=="n":
                print("found but not closed")
                return 2
            else:
                continue
    return -1
    
    
#______________________________________________________________________________
 
#for testing purpose       
#function to dipslay the list
def displayall():
    for ob in lst:
        print(ob)
#______________________________________________________________________________

#Driver code
#menu driven program using match case(switch case) to display menu and take input
choice = 0
while choice!=7:
    choice=int(input("""
                     1.Create new Account
                     2.Withdraw
                     3.Deposit
                     4.Change Pin
                     5.Check Balance
                     6.Close Account
                     7.Exit
                      Enter here: """))
    match choice:
        case 1:
            ch=input("""enter the type of account 
                   a. Savings account
                   b. Current account
                   c. Demat account
                   Enter here: """)
            addnewAccount(ch)
            
        case 2:
            i=input("Enter your id: ")
            pin=int(input("Please enter the PIN: "))
            s=withdraw(i,pin)
            if s==-1:
                print("Wrong id or password")
            
        case 3:
            i=input("Enter your id: ")
            pin=int(input("Please enter the PIN: "))
            s=deposit(i,pin)
            if s==-1:
                print("Wrong id or password")
        case 4:
            i=input("Enter your id: ")
            pin=int(input("Please enter the old PIN: "))
            newpin=int(input("Please enter the new PIN: "))
            s=changePin(i,pin,newpin)
            if s==-1:
                print("Wrong id or password")
        case 5:
            i=input("Enter your id: ")
            s=checkBalance(i)
            if s==-1:
                print("Account not found")
        case 6:
            i=input("Enter your id: ")
            pin=int(input("Please enter the PIN: "))
            s=closeAcc(i,pin)
            if s==-1:
                print("Wrong id or password")
        case 7:
            print("Thankyou for trying our Banking program")
#______________________________________________________________________________
#for testing purpose on;y
#        case 8:
#            displayall()
#______________________________________________________________________________

        case _:
            print("Oops, you have entered wrong choice, Try again")
            
            
#_____________________Thank you for trying our program_________________________




