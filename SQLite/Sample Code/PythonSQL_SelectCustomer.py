import sqlite3
import time

conn = sqlite3.connect('BankAccounts.db')
c = conn.cursor()

# Initialize cache
cache = {}

for i in range(10):
    customerName = input("Enter a First Name: ")

    # Check if the customer name is in the cache
    if customerName in cache:
        # Measure start time for cache retrieval
        start_time = time.time()

        results = cache[customerName]

        # Measure end time for cache retrieval
        end_time = time.time()

        # Calculate runtime for cache retrieval
        cache_runtime = end_time - start_time

        print("Retrieved from cache")
        print(f"Cache retrieval runtime: {cache_runtime:.6f} seconds")
    else:
        # Measure start time for database query
        start_time = time.time()

        cursor = conn.execute('''\
                    SELECT Customer.CustomerID, Customer.FirstName, Customer.LastName
                    FROM Customer
                    WHERE Customer.FirstName = ?''', (customerName,))

        # Fetch all results
        results = cursor.fetchall()

        # Measure end time for database query
        end_time = time.time()

        # Calculate runtime for database query
        db_runtime = end_time - start_time

        # Store the result in the cache
        cache[customerName] = results

        print(f"Query runtime: {db_runtime:.6f} seconds")

    if results:
        for account in results:
            print(account)
    else:
        print("Customer not found.")

conn.close()
