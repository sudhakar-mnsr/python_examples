class Account:
   def __init__(self,acctnum,balance):
     self.accountnum=acctnum
     self.balance=balance
   def __str__(self):
     retStr="Account No: " + str(self.accountnum) \
            + "Balance: " + str(self.balance) 
     return retStr
   def deposit(self,amount):
       self.balance+=amount
class Checking(Account):
   def __init__(self,acctnum,balance,fee):
       Account.__init__(self,acctnum,balance)
       self.fee=fee
   def __str__(self):
     retStr="Account type checking\n" 
     retStr+=Account.__str__(self)
     return retStr
   def withdraw(self,amount):
     if self.balance < amount:
        print "Insufficient funds"
     else:
        self.balance=self.balance-(amount+self.fee)
class Savings(Account):
   def __init__(self,acctnum,balance):
       Account.__init__(self,acctnum,balance)
   def __str__(self):
       retStr="Account type savings\n"
       retStr+=Account.__str__(self)
       return retStr
   def withdraw(self,amount):
       if self.balance < amount:
          print "Insufficient funds"
       else:
          self.balance-=amount  

ca=Checking("123",500,.50)
#print ca
ca.withdraw(200)
ca.deposit(100)
print ca
sa=Savings("456",400)
sa.withdraw(100)
sa.deposit(50)
print sa
accounts=[ca,sa]
for i in range(0,len(accounts)):
    print accounts[i]
