class Account:
   def __init__(self,acctnum,balance):
     self.accountnum=acctnum
     self.balance=balance
   def __str__(self):
     retStr="Account No: " + str(self.accountnum) \
            + "Balance: " + str(self.balance) 
     return retStr
class Checking(Account):
   def __init__(self,acctnum,balance,fee):
       Account.__init__(self,acctnum,balance)
       self.fee=fee
   def __str__(self):
     retStr="Account type checking\n" 
     retStr+=Account.__str__(self)
     return retStr
   def deposit(self, amount):
     self.balance+=amount
   def withdraw(self,amount):
     if self.balance < amount:
        print "Insufficient funds"
     else:
        self.balance=self.balance-(amount+self.fee)

ca=Checking("123",500,.50)
print ca
ca.withdraw(200)
ca.deposit(100)
print ca
