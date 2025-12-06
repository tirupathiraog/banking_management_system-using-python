import pickle
import os

DATA_FILE = "accounts.pkl"

def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as file:
            return pickle.load(file)

def save_accounts(accounts):
    with open(DATA_FILE, "wb") as file:
        pickle.dump(accounts, file)

def new_account(accounts):
    acc = input("Account number: ")
    if acc in accounts:
        print("Account exists")
        return
    name = input("Name: ")
    bal = float(input("Initial deposit: "))
    accounts[acc] = {"name": name, "balance": bal}
    print("Account created")

def deposit(accounts):
    acc = input("Account number: ")
    if acc in accounts:
        amt = float(input("Amount: "))
        accounts[acc]["balance"] += amt
        print("Deposited")
    else:
        print("Account not found")

def withdraw(accounts):
    acc = input("Account number: ")
    if acc in accounts:
        amt = float(input("Amount: "))
        if accounts[acc]["balance"] >= amt:
            accounts[acc]["balance"] -= amt
            print("Withdrawn")
        else:
            print("Insufficient balance")
    else:
        print("Account not found")

def check_balance(accounts):
    acc = input("Account number: ")
    if acc in accounts:
        print("Balance:", accounts[acc]["balance"])
    else:
        print("Account not found")

def display(accounts):
    for acc, data in accounts.items():
        print(acc, data["name"], data["balance"])

def close_account(accounts):
    acc = input("Account number: ")
    if acc in accounts:
        del accounts[acc]
        print("Account closed")
    else:
        print("Account not found")

def main():
    accounts = load_accounts()
    if accounts is None:
        accounts = {}

    while True:
        print("\n1.New 2.Deposit 3.Withdraw 4.Balance 5.Display 6.Close 7.Exit")
        ch = input("Choice: ")

        if ch == "1":
            new_account(accounts)
        elif ch == "2":
            deposit(accounts)
        elif ch == "3":
            withdraw(accounts)
        elif ch == "4":
            check_balance(accounts)
        elif ch == "5":
            display(accounts)
        elif ch == "6":
            close_account(accounts)
        elif ch == "7":
            save_accounts(accounts)
            print("Data saved")
            break
        else:
            print("Invalid choice")

main()
