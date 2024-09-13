
import sqlite3


conn = sqlite3.connect('BankAccounts.db')

c = conn.cursor()

c.execute('SELECT * FROM Account ')
accounts = c.fetchall()
for account in accounts:
    print (account)

c.execute('SELECT * FROM Customer ')
customers = c.fetchall()
for customer in customers:
    print (customer)

conn.close()
    

