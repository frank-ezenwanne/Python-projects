#Uncomment the code at the bottom to run some functions..


class Account:
    def __init__(self,firstnm,lastnm,balance):
        self.firstnm = firstnm
        self.lastnm = lastnm
        self.full_name = firstnm + " " + lastnm
        self.balance = balance 

    def make_deposit(self):
        try:
            print(self.full_name)
            deposit = float(input("how much do you wanna deposit today ?\n"))
            if int(deposit) != deposit:
                print("You can only use whole numbers")
                self.make_deposit()
               
             
            if deposit % 10 != 0 and deposit % 10 != 5:
                """return
            the last digit...Mehnnn..Thank GOD for d modulus operator in d python
            material u guys dropped..It saved d day"""
                print("The Nigerian currency does not allow for such amounts")
                self.make_deposit()
            else:
                self.balance += deposit
                print(self.full_name,"Your balance is now",self.balance)
                return               
        except:
            ValueError
            print("Input a real number")
            self.make_deposit()

    def make_withdrawal(self):
        if self.balance < 1000:
            print("Sorry you cannot withdraw because your balance is below 1000")
            return 
            """Teenoh..thanks for the return statement..didn't see 
            that coming!!!!"""
        try:
            print(self.full_name)
            debit = float(input("How much do you wanna withdraw today ?\n"))
            if int(debit) != debit:
                print("You can only use whole numbers")
                self.make_withdrawal()
                
            if debit % 10 != 0 and debit % 10 != 5:
                print("The Nigerian currency does not allow for such amounts")
                self.make_withdrawal()
                
            if debit > self.balance:
                print("Not enough balance")
                return 
            self.balance -= debit
            print(self.full_name,"Your balance is now",self.balance)
        except:
            ValueError
            print("Input a real number")
            self.make_withdrawal()

account1 = Account("Zen","Johnson",5000)
account2 = Account("Sherlock","Wayne",900)

#print(account1.make_deposit())
#print(account2.make_deposit())

#print(account1.make_withdrawal())
#print(account2.make_withdrawal())




##bankapp
##DSC_Uniben
##checkout DSC
##groundnut n git people
##crazy-tech
##CodeMad
##I don't know what crazy-tech and CodeMad are!





