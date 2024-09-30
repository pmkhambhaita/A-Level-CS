import sqlite3
import time

conn = sqlite3.connect('BankAccounts.db')
c = conn.cursor()

for i in range(10):
    customerName = input("Enter a First Name: ")

    # Measure start time
    start_time = time.time()

    cursor = conn.execute('''\
                SELECT Customer.CustomerID, Customer.FirstName, Customer.LastName
                FROM Customer
                WHERE Customer.FirstName = ?''', (customerName,))

    # Measure end time
    end_time = time.time()

    # Calculate runtime
    runtime = end_time - start_time

    for account in cursor:
        print(account)

    print(f"Query runtime: {runtime:.6f} seconds")

conn.close()
