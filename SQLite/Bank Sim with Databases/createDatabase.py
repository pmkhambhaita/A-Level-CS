import sqlite3

conn = sqlite3.connect('BankAccounts.db')
c = conn.cursor()

# Create Account table
c.execute('''CREATE TABLE Account
             (AccountID text, CustomerID int, Balance real)''')

# Insert data into Account table
c.execute("INSERT INTO Account VALUES ('JBLAcc1001', 1, 35.14)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1002', 2, 150.0)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1003', 3, 12.75)")

# Create Customer table with PIN column
c.execute('''CREATE TABLE Customer
             (CustomerID int, FirstName text, LastName text, PIN text)''')

# Insert data into Customer table
c.execute("INSERT INTO Customer VALUES (1, 'Bob', 'Smith', '1234')")
c.execute("INSERT INTO Customer VALUES (2, 'Jim', 'Wilson', '5678')")
c.execute("INSERT INTO Customer VALUES (3, 'Willie', 'Johnson', '9101')")

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
