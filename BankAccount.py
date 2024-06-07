


class Account:
    cnt=1
    @staticmethod
    def __generatecode(atype):
        aid=atype+str(Account.cnt)
        
        return aid
        
    def __init__(self,name="",pin=0,balance=0,aid=0,atype=""):
        if aid==0:
            self.__aid=Account.__generatecode(atype)
        else:
            self.__aid=aid
        Account.cnt=Account.cnt+1
        
        self.__name=name
        self.__pin=pin
        self._balance=balance
        
    def set_aid(self,aid):
        self.__aid=aid
        
    def get_aid(self):
        return self.__aid
    
    def set_name(self,name):
        self.__name=name
        
    def get_name(self):
        return self.__name
    
    def set_balance(self,balance):
        self._balance=balance
        
    def get_balance(self):
        return self._balance
    
    def set_pin(self,pin):
        self.__pin=pin
        
    def get_pin(self):
        return self.__pin
    
    
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self._balance = self._balance+amount
        print("\n Amount Deposited:",amount)
    
    
            
   
    def __str__(self):
        return f"Id: {self.__aid} Name: {self.__name} PIN: {self.__pin} Balance:{self._balance}"
    


class Savingacc(Account):
    __minbal=2000
    __intrt=2.0
    
    def __init__(self,name="",pin=0,balance=0,ecs=0,aid=0,atype="s"):
        #call parent constructor
        super().__init__(name,pin,balance,aid,atype)
        self.__ecs=ecs
        
    def set_ecs(self,ecs):
        self.__ecs=ecs
        
    def get_ecs(self):
        return self.__ecs
    
    def get_minbal(self):
        return self.__minbal
    
    def get_intrt(self):
        return self.__intrt
    
    #def __str__(self):
    def __str__(self):
        s=super().__str__()+f" ECS={self.__ecs}"
        return s  
    
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        __bal=self._balance-amount
        if __bal>=self.__minbal:
            self._balance=__bal
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
        
        
        
                
    
class Currentacc(Account):
    __minbal=10000
    __intrt=3.0
    
    def __init__(self,name="",pin=0,balance=0,ntr=0,aid=0,atype="c"):
        #call parent constructor
        super().__init__(name,pin,balance,aid,atype)
        self.__ntr=ntr
    def set_ntr(self,ntr):
        self.__ntr=ntr
        
    def get_ntr(self):
        return self.__ntr
    
    def get_minbal(self):
        return self.__minbal
    
    def get_intrt(self):
        return self.__intrt
    
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        __bal=self._balance-amount
        if __bal>=self.__minbal:
            self._balance=__bal
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    
    def __str__(self):
        return super().__str__()+f" No. of Transaction={self.__ntr}"







class Dematacc(Account):
    __minbal=50000
    __intrt=5.0
    
    def __init__(self,name="",pin=0,balance=0,com=0,aid=0,atype="d"):
        #call parent constructor
        super().__init__(name,pin,balance,aid,atype)
        self.__com=com
    def set_com(self,com):
        self.__com=com
        
    def get_com(self):
        return self.__com
    
    def get_minbal(self):
        return self.__minbal
    
    def get_intrt(self):
        return self.__intrt
    
    def __str__(self):
        return super().__str__()+f" COMISSION={self.__com}"
    
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        __bal=self._balance-amount
        if __bal>=self.__minbal:
            self._balance=__bal
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
            
            
            
            
#________________________________________________________________
    
if __name__=="__main__":
    ob1=Savingacc("Ayush Swami",1111,2500,50)
    print(ob1)
#    ob1.withdraw()
 #   print(Account.get_balance(ob1))
    
#________________________________________________________________    
    
    
    
    
    
    
    
    
    
