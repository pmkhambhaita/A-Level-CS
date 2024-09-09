
import sqlite3


conn = sqlite3.connect('BankAccounts.db')

c = conn.cursor()

cursor = conn.execute ('''\
            SELECT AccountID, Balance FROM Account''')

balances = cursor.fetchall()

for account in balances:   
    print(account)
    accountID = account[0]
    balance = float(account[1])
    balance += 5
    cursor = conn.execute ('''\
            UPDATE Account SET Balance = ? WHERE AccountID = ?''',(balance,accountID))

conn.commit()

cursor = conn.execute ('''\
            SELECT AccountID, Balance FROM Account''')

balances = cursor.fetchall()
for account in balances:   
    print(account)

    
conn.close()
    

