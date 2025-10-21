class SavingsAccount:
    def __init__(self, name, balance, pin, is_active=True):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.is_active = is_active
        self.daily_limit = 10000  
        self.atm_requested = False
        self.cheque_requested = False

    
    def check_balance(self, entered_pin):
        print("Checking Balance")
        if entered_pin != self.pin:
            print("Incorrect PIN")
        elif not self.is_active:
            print("Account is inactive (frozen)")
        else:
            print(f"Balance: ₹{self.balance}")

    
    def withdraw(self, amount, entered_pin):
        print("Withdraw Funds")
        if entered_pin != self.pin:
            print(" Incorrect PIN")
        elif not self.is_active:
            print("Account is inactive (frozen)")
        elif amount > self.balance:
            print(" Insufficient balance.")
        elif amount > self.daily_limit:
            print(f" Amount exceeds daily limit of ₹{self.daily_limit}")
        else:
            self.balance -= amount
            print(f" Withdrawn ₹{amount}. New Balance: ₹{self.balance}")

    
    def deposit(self, amount, entered_pin):
        print("Deposit Funds")
        if entered_pin != self.pin:
            print("Incorrect PIN.")
        elif amount <= 0:
            print(" Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print(f" Deposited ₹{amount}. New Balance: ₹{self.balance}")

    
    def request_atm_card(self):
        print("ATM Card Request")
        if self.atm_requested:
            print(" ATM card already requested")
        else:
            self.atm_requested = True
            print("ATM card request approved")

    
    def request_cheque_book(self):
        print("Cheque Book Request")
        if self.cheque_requested:
            print("Cheque book already requested")
        else:
            self.cheque_requested = True
            print("Cheque book request approved")

    
    def freeze_account(self):
        print("Freeze Account")
        if not self.is_active:
            print(" Account already frozen")
        else:
            self.is_active = False
            print("Account has been frozen")

    
    def unfreeze_account(self):
        print("Unfreeze Account")
        if self.is_active:
            print("Account already active")
        else:
            self.is_active = True
            print(" Account has been unfrozen and is now active")





s1 = SavingsAccount("sai", 10000, 1234)


s1.check_balance(1234)     
  
s1.withdraw(2000, 1111)    
    
s1.deposit(1000, 1111)     
    
s1.request_atm_card()      


s1.request_cheque_book()  
  
        
s1.freeze_account()       
     
s1.unfreeze_account()      
