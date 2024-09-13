
import sqlite3


conn = sqlite3.connect('BankAccounts.db')

c = conn.cursor()

customerName=input("Enter a First Name: ")

cursor = conn.execute ('''\
            SELECT Customer.CustomerID,Customer.FirstName, Customer.LastName
            FROM Customer
            WHERE Customer.FirstName = ?''', (customerName,))

for account in cursor:
    print(account)

conn.close()
    

