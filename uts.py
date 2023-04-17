class Atm:
    def __init__(self):
        self.pin = 123
        self.balance = 15000
        self.menu()
    def menu(self):
        print("""
            what would you like to do!
                1. Check balance   
                2. Withdraw balance 
                3. Deposit balance
                     """)
        
        option = int(input("enter your option: "))
        if option == 1:
            self.Check_balance()
        elif option == 2:
            self.Withdraw()
        elif option == 3:
            self.Deposit()
       


    def Check_balance(self):
        input_pin = int(input("enter your pin: "))
        if input_pin == self.pin:
            print("*" * 50)
            print(f"your balance is {self.balance}")
            print("*" * 50) 
        else:
            print("you pin is incorrect")
        self.menu()


    def Withdraw(self):
        input_pin = int(input("enter your pin: "))
        if input_pin == self.pin:
            input_balance = int(input("enter your Withdraw amount: "))
            if input_balance <= self.balance:
                self.balance = self.balance - input_balance
                print("*" * 50)
                print(f"your updated balance is {self.balance}")
                print("*" * 50)
            else:
                print("you don't have that much balance! ")
        else:
            print("your pin is incorrect! ")
        self.menu()


    def Deposit(self):
        input_pin = int(input("enter your pin: "))
        if input_pin == self.pin:
            input_Deposit = int(input("enter your Deposit amount:"))
            self.balance = self.balance + input_Deposit
            print("*" * 50)
            print(f"your updated balance is {self.balance}")
            print("*" * 50)
        else:
            print("you pin is incorrect!")
       
sbi = Atm()

 