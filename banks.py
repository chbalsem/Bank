# Base Client class
class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.accounts = []

    def get_CIN(self): return self.__CIN
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName
    def get_tel(self): return self.__tel
    def set_tel(self, tel): self.__tel = tel

    def display(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")

    def add_account(self, account):
        self.accounts.append(account)

    def list_accounts(self):
        for acc in self.accounts:
            print(f"Account Code: {acc.get_code()}, Balance: {acc.get_balance()} DA")


# Base Account class
class Account:
    __nbAccounts = 0

    def __init__(self, owner: Client):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner
        self.record = []
        owner.add_account(self)

    def get_code(self): return self.__code
    def get_balance(self): return self.__balance
    def get_owner(self): return self.__owner

    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.record.append(f"Credited {amount}DA")
        else:
            raise ValueError("Wrong amount")

    def debit(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                self.record.append(f"Debited {amount}DA")
            else:
                raise ValueError("Insufficient balance")
        else:
            raise ValueError("Wrong amount")

    def transfer_to(self, amount, other_account):
        self.debit(amount)
        other_account.credit(amount)
        self.record.append(f"Transferred {amount}DA to Account {other_account.get_code()}")
        other_account.record.append(f"Received {amount}DA from Account {self.get_code()}")

    def display(self):
        owner = self.__owner
        print(f"Account Code: {self.__code}")
        print(f"Owner: {owner.get_firstName()} {owner.get_lastName()}")
        print(f"Balance: {self.__balance} DA")

    def displayTransactions(self):
        print(f"Transaction history: {self.record}")

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)


# Primary subclass of Account
class Primary(Account):
    __nPrimaryAcc = 0

    def __init__(self, owner: Client):
        super().__init__(owner)  # call Account constructor
        Primary.__nPrimaryAcc += 1

    @staticmethod
    def displayNbPrimary():
        print("Total primary accounts created:", Primary.__nPrimaryAcc)


# -----------------------
# Example usage
c1 = Client("Bouberna", "Souaad", "0799865543")
c2 = Client("Chaibai", "Assma", "0799005543")

# Create Primary accounts
p1 = Primary(c1)
p2 = Primary(c2)

Primary.displayNbPrimary()  # 2

# Regular accounts
acc1 = Account(c1)
acc2 = Account(c1)

acc1.credit(3000)
acc1.transfer_to(3000, acc2)

acc1.display()
acc1.displayTransactions()
acc2.display()
acc2.displayTransactions()
Account.displayNbAccounts()
c1.list_accounts()
