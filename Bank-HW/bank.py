import json

import random
import string

import os



class User:
    FILE_NAME = 'bank.json'

    # Init Functions

    def __init__(self, f_name, l_name, start_balance, id="Default"):
        if id == "Default":                             # Правим тази проверка, защото човек може да
            self.id = self.id_generator()               # да поиска да си използва стария
            self.f_name = f_name                        # (вече съществуващ) акаунт, вместо да отваря нов
            self.l_name = l_name
            self.accounts = self.read_accounts()
            self.open_account(start_balance)
        else:                                           # Ако ни е подаден съществуващ акаунт
            self.id = id
            self.accounts = self.read_accounts()

    @staticmethod                                       # Ако не се използва '@staticmethod' - не работи в класа
    def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def open_account(self, balance):                                                    # С True показваме, че е нов акаунт, защото
        self.accounts.append(BankAccount(self.id, self.id_generator(), balance, True))  # използваме същата функция при логване на акаунтите

    # File Functions
    @staticmethod           # Същото както коментара на 26ти ред - https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/
    def write_json(data):
        with open(User.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    def read_accounts(self):
        if os.path.exists(User.FILE_NAME) and not os.stat(User.FILE_NAME).st_size == 0: # Правим тази двойна проверка, 
            with open(User.FILE_NAME, "r") as f:                                        # защото файлът може да е празен
                                                                                        # т.е. няма да има главната структура
                data = json.load(f)

                for client in data["Users"]:
                    if client["User ID"] == self.id:
                        return [BankAccount(self.id, acc["IBAN"], acc["Balance"])
                                for acc in client["Accounts"]]

            temp = data["Users"]
            temp.append({
                "User ID": self.id,
                "Names": [{
                    "First": self.f_name,
                    "Last": self.l_name    
                }],
                "Accounts": []
            })
            self.write_json(data)
            return []
        else:
            self.write_json({
                "Users": [{
                    "User ID": self.id,
                    "Names": [{
                        "First": self.f_name,
                        "Last": self.l_name    
                    }],
                    "Accounts": []
                }]
            })
            return []
    
    # Transfer Functions

    def deposit(self, iban, balance):
        for acc in self.accounts:
            if acc.iban == iban:
                acc.deposit(balance)
                return

    def withdraw(self, iban, balance):
        for acc in self.accounts:
            if acc.iban == iban:
                acc.withdraw(balance)
                return
    
    # Future Functions

    def send_money(self, usr_src, acc_src, usr_dst, acc_dst, ammount):
        self.withdraw(acc_src, ammount)
        '''with open(User.FILE_NAME, "r") as f:
            data = json.load(f)

            for user in data["Users"]:
                if user["User ID"] == usr_dst:
                    for acc in user["Accounts"]:
                        if acc["IBAN"] == acc_dst:
                            acc["Balance"] += ammount
            self.write_json(data) '''
        # To be contiued

    def recieve_money(self, usr_src, acc_src, usr_dst, acc_dst):
        pass

class BankAccount:
    FILE_NAME = 'bank.json'

    # Init Function

    def __init__(self, parent_id, iban, start_balance, is_new=False):
        self.parent_id = parent_id
        self.iban = iban
        self.balance = self.first_write(start_balance) if is_new else start_balance

    # File Functions

    @staticmethod
    def write_json(data):
        with open(BankAccount.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)
    
    def first_write(self, balance):                     # Ако за първи път записваме - правим структура
        with open(BankAccount.FILE_NAME, "r") as f:
            data = json.load(f)

            for user in data["Users"]:
                if user["User ID"] == self.parent_id:
                    temp = user["Accounts"]
                    temp.append({
                        "IBAN": self.iban,
                        "Balance": balance
                    })
                    self.write_json(data)
                    return balance

    def update_file(self):
        with open(BankAccount.FILE_NAME, "r") as f:
            data = json.load(f)

            for client in data["Users"]:
                if client["User ID"] == self.parent_id:
                    for acc in client["Accounts"]:
                        if acc["IBAN"] == self.iban:
                            acc["Balance"] = self.balance

            self.write_json(data)

    # Transfer Functions

    def deposit(self, amount):
        self.balance += amount
        self.update_file()

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("YOU DON'T HAVE ENOUGH RESOURCES TO DO THIS OPERATION")
            return
        self.balance -= amount
        self.update_file()

# Main

user1 = User("Aleko", "Georgiev", 1000)