class SavingsAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin

    def display_details(self):
        print("Savings Account")
        print("Account Holder Name:", self.name)
        print("Initial Balance:", self.balance)
        print("PIN Number:", self.pin)


class BusinessAccount:
    def __init__(self, business_name, balance):
        self.business_name = business_name
        self.balance = balance

    def display_details(self):
        print("Business Account")
        print("Business Name:", self.business_name)
        print("Initial Balance:", self.balance)



s1 = SavingsAccount("sai", 5000, 1234)
s1.display_details()

print()


b1 = BusinessAccount("TechCorp", 25000)
b1.display_details()
