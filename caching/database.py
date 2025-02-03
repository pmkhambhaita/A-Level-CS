import sqlite3
import os
import tkinter as tk
from tkinter import messagebox
import time

def create_database():
    # Check if the database already exists
    if os.path.exists('database1.db'):
        print("Database already exists.")
        return

    # Connect to the database
    conn = sqlite3.connect('database1.db')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE Name
                 (name text, CustomerID int)''')

    # Generate random names and account numbers
    first_names = ['John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie', 'Mike', 'Laura', 'David', 'Sarah']

    for i in range(10):
        c.execute("INSERT INTO Name VALUES (?, ?)", (first_names[i], i + 1))

    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()

def query_database(customer_id):
    start_time = time.time()
    conn = sqlite3.connect('database1.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Name WHERE CustomerID=?", (customer_id,))
    result = c.fetchone()
    conn.close()
    end_time = time.time()
    query_time = (end_time - start_time) * 1000
    print(f"Query time: {query_time:.3f} milliseconds")
    return result

def search():
    customer_id = entry.get()
    if not customer_id.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid Customer ID.")
        return

    result = query_database(int(customer_id))
    if result:
        name_label.config(text=f"Name: {result[0]}\nCustomerID: {result[1]}")
    else:
        name_label.config(text="No record found.")

create_database()

app = tk.Tk()
app.title("Customer Search")

tk.Label(app, text="Enter Customer ID:").pack(pady=5)
entry = tk.Entry(app)
entry.pack(pady=5)

tk.Button(app, text="Search", command=search).pack(pady=5)
name_label = tk.Label(app, text="")
name_label.pack(pady=5)

app.mainloop()