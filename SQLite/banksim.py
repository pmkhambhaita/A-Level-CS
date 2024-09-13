import sqlite3
import os

db_path = 'Accounts.db'

# Check if the database already exists
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''CREATE TABLE Account
                 (Name text, AccountID int,  Balance real)''')
    c.execute("INSERT INTO Account VALUES ('jake',1001,35.14)")
    c.execute("INSERT INTO Account VALUES ('tim',2002, 150.0)")
    c.execute("INSERT INTO Account VALUES ('john',3003,12.75)")

    # Save (commit) the changes
    conn.commit()
    conn.close()

conn = sqlite3.connect(db_path)
c = conn.cursor()

usr_input = input("Enter your first name: ").lower()

# Fetch the balance for the given CustomerID
c.execute("SELECT Balance FROM Account WHERE Name = ?", (usr_input,))
result = c.fetchone()

if result:
    print(f"Balance for CustomerID {usr_input}: £{result[0]}")
else:
    print(f"No account found for CustomerID {usr_input}")

conn.close()

