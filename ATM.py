class ATM():
    def __init__(self, name, atm_card_number, pin, amount):
        self.name = name
        self.atm_card_number = atm_card_number
        self.pin_number = pin
        self.amount = amount

    def cash_withdrawl(self, amount):
        self.amount = self.amount + amount
        print(self.amount)

        option = input(
            "Do you want to check your balance: (yes or no): ")

        if option == "yes":
            self.balance_enquiry()
        else:
            exit

    def balance_enquiry(self):
        print(self.amount)

        option = input(
            "Do you want to add more money: (yes or no): ")

        if option == "yes":
            amount = int(input("Enter amount: "))
            self.cash_withdrawl(amount)
        else:
            exit


name = input("Your name: ")
atm_card_number = input("Your atm card number: ")
pin = input("Your pin: ")
amount = 0

atm = ATM(name, atm_card_number, pin, amount)

option = input("Enter CW for cash withdrawl or BE for balance enquiry: ")

if option == "CW":
    amount = int(input("Enter amount: "))
    atm.cash_withdrawl(amount)
elif option == "BE":
    atm.balance_enquiry()
else:
    exit
