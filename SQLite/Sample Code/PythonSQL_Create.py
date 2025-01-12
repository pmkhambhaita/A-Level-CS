import sqlite3
import random
import string

# Connect to the database
conn = sqlite3.connect('BankAccounts.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE Account
             (AccountID text, CustomerID int, Balance real)''')

c.execute('''CREATE TABLE Customer
             (CustomerID int, FirstName text, LastName text)''')

# Generate random names and account numbers
first_names = ['John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie', 'Mike', 'Laura', 'David', 'Sarah']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']

# Insert data into Customer table
for i in range(10):
    c.execute("INSERT INTO Customer VALUES (?, ?, ?)", (i + 1, first_names[i], last_names[i]))

# Insert data into Account table
for i in range(10):
    account_id = 'ACC' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    balance = round(random.uniform(10.0, 1000.0), 2)
    c.execute("INSERT INTO Account VALUES (?, ?, ?)", (account_id, i + 1, balance))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()