# hdfc bank
# acc holder
    # - name
    # - account number
    # - balance
    # - type of account
# deposit
# withdraw
# balance check
# loan
# new pin set
# statement

# class Bank:
#     name = "HDFC Bank"
#     def __init__(self, acc_num, name, acc_type, pin, bal=5000):
#         self.acc_number = acc_num # TODO: random generate, use random library
#         self.acc_type = acc_type
#         self.name = name
#         self.balance = bal
#         self.atm_pin = pin
#         self.acc_statement = []

#     def show_details(self):
#         print(f"""Account Number: {self.acc_number}
# Account Holder Name: {self.name}
# Account Type: {self.acc_type}
# Account Balance: {self.balance}
# """)
    
#     def show_balance(self):
#         print(f"Your available balance is: {self.balance}")

#     def deposit(self, amt):
#         self.balance += amt
#         print("Amount deposited successfully!")
#         self.acc_statement.append(f"Credit: {amt} - Balance: {self.balance}")
#         self.show_balance()


#     def withdraw(self, amt):
#         if amt > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amt
#             print("Amount withdrawn successfully!")
#             self.acc_statement.append(f"Debit: {amt} - Balance: {self.balance}")
#             self.show_balance()

#     def show_statement(self, num):
#         for i in self.acc_statement:
#             print(i)

#     def update_pin(self, new_pin):
#         if len(new_pin) != 4:
#             print("New pin should be of 4 digits")
#         else:
#             self.atm_pin = new_pin
#             print("New pin updated successfully!")
            
#     # TODO: implement loan
#     # TODO: last 5 statement


# bank_obj = Bank(11224455, "Aditi", "Saving", 5481, 125000)
# # bank_obj.show_details()
# # bank_obj.show_balance()
# # bank_obj.deposit(5000)
# # bank_obj.withdraw(20000)
# c = 0
# while True:
#     print(f"Welcome to {Bank.name}!")
#     user_pin = int(input("Enter your pin:- "))
#     if user_pin != bank_obj.atm_pin:
#         print("Invalid pin.")
#         break
#     print("""########################
# Choose an option:
# SD - Show Details
# B  - Show Balance
# D  - Deposit
# W  - Withdraw
# ST - Statement
# E  - Exit """)
#     user_inp = input("Enter your choice:- ").upper() # SD
#     if user_inp == "SD":
#         bank_obj.show_details()
#     elif user_inp == "B":
#         bank_obj.show_balance()
#     elif user_inp == "D":
#         user_amt = int(input("Enter an amount to be deposited:-"))
#         bank_obj.deposit(user_amt)
#     elif user_inp == "W":
#         user_amt = int(input("Enter an amount to be withdrawn:-"))
#         bank_obj.withdraw(user_amt)
#     elif user_inp == "ST":
#         bank_obj.show_statement()
#     elif user_inp == "E":
#         print(f"Thank you for banking with {Bank.name}! Visit Again!")
#         break
#     else:
#         c += 1
#         if c == 3:
#             print("Too many invalid attempts.")
#             break
#         print("Invalid option. Try again!")






import random
import math

class Loan:
    def __init__(self, principal, interest_rate, tenure_months):
        self.principal = principal
        self.interest_rate = interest_rate  # annual rate in %
        self.tenure = tenure_months  # months
        self.remaining_principal = principal
        self.paid = 0
        self.months_paid = 0
        self.loan_active = True
        self.emi = self.calculate_emi()

    def calculate_emi(self):
        # Monthly interest rate
        r = self.interest_rate / (12 * 100)
        n = self.tenure
        p = self.principal
        if r == 0:
            return p / n
        emi = (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return round(emi, 2)

    def make_payment(self):
        if not self.loan_active:
            print("Loan has already been repaid.")
            return
        interest_for_month = self.remaining_principal * self.interest_rate / (12*100)
        principal_paid = self.emi - interest_for_month
        self.remaining_principal -= principal_paid
        self.paid += self.emi
        self.months_paid += 1
        if self.months_paid >= self.tenure or self.remaining_principal <= 0:
            self.loan_active = False
            self.remaining_principal = 0
            print("Loan repaid fully!")
        return (self.emi, round(principal_paid,2), round(interest_for_month,2))

    def show_loan(self):
        print(f'''Loan Principal: {self.principal}
Interest Rate: {self.interest_rate}%
Tenure: {self.tenure} months
Monthly EMI: {self.emi}
Remaining Principal: {round(self.remaining_principal,2)}
Loan Active: {self.loan_active}
Months Paid: {self.months_paid}
Total Paid: {round(self.paid,2)}
''')


class Bank:
    name = "HDFC Bank"
    def __init__(self, acc_num=None, name="", acc_type="", pin=0, bal=5000):
        if acc_num is None:
            self.acc_number = random.randint(10000000, 99999999)
        else:
            self.acc_number = acc_num
        self.acc_type = acc_type
        self.name = name
        self.balance = bal
        self.atm_pin = pin
        self.acc_statement = []
        self.loan_account = None
        self.loan_history = []

    def show_details(self):
        print(f"""Account Number: {self.acc_number}
Account Holder Name: {self.name}
Account Type: {self.acc_type}
Account Balance: {self.balance}
""")

    def show_balance(self):
        print(f"Your available balance is: {self.balance}")

    def deposit(self, amt):
        self.balance += amt
        print("Amount deposited successfully!")
        self.acc_statement.append(f"Credit: {amt} - Balance: {self.balance}")
        self.show_balance()

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amt
            print("Amount withdrawn successfully!")
            self.acc_statement.append(f"Debit: {amt} - Balance: {self.balance}")
            self.show_balance()

    def show_statement(self):
        print("Last 5 transactions:")
        for i in self.acc_statement[-5:]:
            print(i)

    def update_pin(self, new_pin):
        if len(str(new_pin)) != 4:
            print("New pin should be of 4 digits")
        else:
            self.atm_pin = new_pin
            print("New pin updated successfully!")

    def apply_loan(self, amount, interest, tenure):
        # Eligibility check: only one active loan, minimum balance or income
        if self.loan_account and self.loan_account.loan_active:
            print("You already have an active loan.")
            return
        if amount <= 0 or interest < 0 or tenure <= 0:
            print("Enter valid amount, interest rate, and tenure.")
            return
        if self.balance < 1000:  # Assume minimum balance requirement
            print("Insufficient balance to apply for a loan, maintain minimum balance.")
            return
        self.loan_account = Loan(amount, interest, tenure)
        self.balance += amount
        self.loan_history.append({
            'amount': amount,
            'interest_rate': interest,
            'tenure': tenure,
            'EMI': self.loan_account.emi
        })
        self.acc_statement.append(f"Loan credited: {amount} - Balance: {self.balance}")
        print(f"Loan of Rs {amount} approved at {interest}% for {tenure} months. EMI: {self.loan_account.emi}")
        self.show_balance()

    def repay_loan(self):
        if not self.loan_account or not self.loan_account.loan_active:
            print("No active loan to repay.")
            return
        if self.balance < self.loan_account.emi:
            print("Insufficient balance to pay EMI.")
            return
        emi, principal_paid, interest_paid = self.loan_account.make_payment()
        self.balance -= emi
        self.acc_statement.append(f"Loan EMI paid: {emi} - Principal: {principal_paid}, Interest: {interest_paid} - Balance: {self.balance}")
        print(f"EMI of Rs {emi} paid. Principal: {principal_paid}, Interest: {interest_paid}")
        if not self.loan_account.loan_active:
            self.acc_statement.append("Loan closed.")
            print("Congratulations! Your loan is fully repaid.")

    def show_loan(self):
        if not self.loan_account:
            print("No loan is present.")
            return
        self.loan_account.show_loan()

    def show_loan_history(self):
        if not self.loan_history:
            print("No loan history found.")
            return
        print("Loan History:")
        for idx, hist in enumerate(self.loan_history, 1):
            print(f"Loan {idx}: Amount: {hist['amount']}, Interest: {hist['interest_rate']}%, Tenure: {hist['tenure']} months, EMI: {hist['EMI']}")

# Sample main interaction loop

bank_obj = Bank(None, "Mayank", "Saving", 1965, 125000)
c = 0
while True:
    print(f"Welcome to {Bank.name}!")
    try:
        user_pin = int(input("Enter your pin:- "))
    except Exception:
        print("Invalid input. Pin should be numbers.")
        break
    if user_pin != bank_obj.atm_pin:
        print("Invalid pin.")
        break
    print("""########################
Choose an option:
SD - Show Details
B  - Show Balance
D  - Deposit
W  - Withdraw
ST - Statement
AL - Apply for Loan
RL - Repay Loan EMI
SL - Show Loan Details
LH - Loan History
E  - Exit """)
    user_inp = input("Enter your choice:- ").upper()
    if user_inp == "SD":
        bank_obj.show_details()
    elif user_inp == "B":
        bank_obj.show_balance()
    elif user_inp == "D":
        user_amt = int(input("Enter an amount to be deposited:-"))
        bank_obj.deposit(user_amt)
    elif user_inp == "W":
        user_amt = int(input("Enter an amount to be withdrawn:-"))
        bank_obj.withdraw(user_amt)
    elif user_inp == "ST":
        bank_obj.show_statement()
    elif user_inp == "AL":
        amt = int(input("Enter loan amount:-"))
        rate = float(input("Enter annual interest rate (in %):-"))
        tenure = int(input("Enter tenure (in months):-"))
        bank_obj.apply_loan(amt, rate, tenure)
    elif user_inp == "RL":
        bank_obj.repay_loan()
    elif user_inp == "SL":
        bank_obj.show_loan()
    elif user_inp == "LH":
        bank_obj.show_loan_history()
    elif user_inp == "E":
        print(f"Thank you for banking with {Bank.name}! Visit Again!")
        break
    else:
        c += 1
        if c == 3:
            print("Too many invalid attempts.")
            break
        print("Invalid option. Try again!")
