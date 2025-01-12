
import sqlite3


conn = sqlite3.connect('BankAccounts.db')

c = conn.cursor()

cursor = conn.execute ('''\
            SELECT Account.AccountID, Customer.FirstName, Customer.LastName, Account.Balance
            FROM Account
            INNER JOIN Customer
            ON Account.CustomerID = Customer.CustomerID  ''')

for account in cursor:
    print(account)


conn.close()
    

