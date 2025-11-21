import re
p=r"^\+998\d{9}$"
class Card:
    def __init__(self,owner, card_number, balance, password, phone_number=None):
        self.owner = owner
        self.card_number = card_number
        self.balance = balance
        self.password = password
        self.phone_number = phone_number

s1=Card("Sardor", "123456789012", "50000", "0000", "+998888888888")
s2=Card("Alisher", "0011223344556677", "30000", "1111", None)
s3=Card("Bobur", "0000111122223333", "10000", "5555", None)
base=[s1, s2, s3]

class ATM:
    def __init__(self,bank):
        self.bank = bank
        self.card=None

    def authentication(self):
        card_number=input(" Please enter the card number:\n ").strip()
        if not card_number.isdigit():
            print("Enter only numbers")
            return False
        for i in base:
            if i.card_number==card_number:
                self.card=i
                break
        if self.card==None:
            print("Card not found")
            return False
        password=input("Please enter the password:").strip()
        if not password.isdigit():
            print("Enter only numbers")
            return False
        if password !=self.card.password:
            print("Passwords do not match")
            self.card=None
            return False
        print(f"Welcome {self.card.owner}")
        return True
    def view_balance(self):
        print(f"Your balance is {self.card.balance}")
    def deposit(self):
        amount=input(f" Your balance is {self.card.balance}.\n How much do you want to deposit?\n ").strip()
        if not amount.isdigit():
            print("Enter only numbers")
            return False
        amount=int(amount)
        if amount<0:
            print("Amount cannot be negative")
            return False
        self.card.balance+=amount
        print(f" Your new balance is {self.card.balance}\n")
    def withdraw(self):
        amount=input(f" Your balance is {self.card.balance}.\n How much do you want to withdraw?\n ").strip()
        if not amount.isdigit():
            print("Enter only numbers")
            return False
        amount=int(amount)
        if amount<0:
            print("Amount cannot be negative")
            return False
        if amount>self.card.balance:
            print("You don't have enough money")
            return False
        self.card.balance-=amount
        print(f" Your new balance is {self.card.balance}\n")
    def sms_on(self):
        if self.card.phone_number is not None:
            print(f"Your sms system is already on,\n Your number is {self.card.phone_number}")
            return False
        phone_number=input(" Please enter your phone number:\n ").strip()
        if not re.match(p,phone_number):
            print("Invalid phone number")
            return False
        self.card.phone_number=phone_number
        print(f" Sms system is turned on in {self.card.phone_number} number.\n")
    def sms_off(self):
        if self.card.phone_number is None:
            print("You don't have any phone number")
            return False
        print(" Sms system is turned off")
        self.card.phone_number=None
    def change_password(self):
        old_password=input("Please enter the old password:").strip()
        if old_password!=self.card.password:
            print("Passwords do not match")
            return False
        new_password=input("Please enter the new password:").strip()
        if not new_password.isdigit():
            print("Enter only numbers")
            return False
        if new_password == self.card.password:
            print("Your old password and new password are identical.")
            return False
        if len(new_password)!=4:
            print("Password should be made off 4 digits")
            return False
        self.card.password=new_password
        print("Password changed")
    def manager(self):
        while True:
            kod=input(" 1. View balance\n 2. Deposit\n 3. Withdraw\n 4. Change password\n 5. Turn on sms system\n 6. Turn off sms system\n 7. Exit").strip()
            if kod=="1":
                self.view_balance()
            elif kod=="2":
                self.deposit()
            elif kod=="3":
                self.withdraw()
            elif kod=="4":
                self.change_password()
            elif kod=="5":
                self.sms_on()
            elif kod=="6":
                self.sms_off()
            elif kod=="7":
                break
            else:
                print("Please enter a valid option")
                continue
atm=ATM("Hamkor bank")
if atm.authentication():
    atm.manager()