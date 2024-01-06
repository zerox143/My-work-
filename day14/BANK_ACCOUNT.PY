#define the bank account 
class Bankaccount:


 #constructor to initialize balance
  def __init__(self,initial_balance=0):
      self.balance = initial_balance
 #method to deposit money
  def deposit(self,amount):
   self.balance+= amount
   print(f"Deposit${amount} New Balance:${self.balance}")
    #method to widraw money 
  def withdraw(self,amount):
     if amount<=self.balance:
        self.balance-=amount
        print(f"Withdraw: ${amount}New Balance: ${self.balance}")
     else:
        print("Insufficiant Balance")
#Example usage:
#Create abank account instance and perform transactions
account=Bankaccount(1000)
account.deposit(500)
account.withdraw(300)





#example usage
#create abank account instance and perform transaction 