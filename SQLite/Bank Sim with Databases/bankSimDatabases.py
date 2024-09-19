import sqlite3
import tkinter as tk
from tkinter import messagebox
import threading

def get_customer_id(name):
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("SELECT CustomerID FROM Customer WHERE LOWER(FirstName || ' ' || LastName) = ?", (name.lower(),))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def get_balance_by_name(first_name, last_name):
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("""
        SELECT Balance
        FROM Account
        JOIN Customer ON Account.CustomerID = Customer.CustomerID
        WHERE LOWER(Customer.FirstName) = ? AND LOWER(Customer.LastName) = ?
    """, (first_name.lower(), last_name.lower()))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def get_balance_by_id(customer_id):
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("""
        SELECT Balance
        FROM Account
        WHERE CustomerID = ?
    """, (customer_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def transfer_money():
    sender_input = sender_entry.get().lower()
    receiver_input = receiver_entry.get().lower()
    try:
        amount = float(amount_entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be positive")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid amount")
        return

    if sender_input.isdigit():
        sender_id = int(sender_input)
    else:
        sender_id = get_customer_id(sender_input)

    if receiver_input.isdigit():
        receiver_id = int(receiver_input)
    else:
        receiver_id = get_customer_id(receiver_input)

    if sender_id is None or receiver_id is None:
        messagebox.showerror("Error", "Invalid customer ID or name(s)")
        return

    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()

    # Debit sender
    c.execute("UPDATE Account SET Balance = Balance - ? WHERE CustomerID = ?", (amount, sender_id))
    # Credit receiver
    c.execute("UPDATE Account SET Balance = Balance + ? WHERE CustomerID = ?", (amount, receiver_id))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Transfer completed")
    print_balances()

def print_balances():
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("""
        SELECT Customer.FirstName, Customer.LastName, Account.Balance
        FROM Account
        JOIN Customer ON Account.CustomerID = Customer.CustomerID
    """)
    balances = c.fetchall()
    conn.close()

    balance_text.delete(1.0, tk.END)
    for account in balances:
        balance_text.insert(tk.END, f"{account[0]} {account[1]}: £{account[2]:.2f}\n")

    # Clear the balance display after 5 seconds
    balance_text.after(5000, lambda: balance_text.delete(1.0, tk.END))

def show_customer_balance():
    input_value = customer_name_entry.get().lower()
    if input_value.isdigit():
        customer_id = int(input_value)
        balance = get_balance_by_id(customer_id)
        if balance is not None:
            messagebox.showinfo("Balance", f"Customer ID {customer_id}'s balance: £{balance:.2f}")
        else:
            messagebox.showerror("Error", "Customer not found")
    else:
        try:
            first_name, last_name = input_value.split()
            balance = get_balance_by_name(first_name, last_name)
            if balance is not None:
                messagebox.showinfo("Balance", f"{first_name} {last_name}'s balance: £{balance:.2f}")
            else:
                messagebox.showerror("Error", "Customer not found")
        except ValueError:
            messagebox.showerror("Error", "Please enter both first and last names")

def get_next_customer_id():
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("SELECT MAX(CustomerID) FROM Customer")
    result = c.fetchone()
    conn.close()
    return result[0] + 1 if result[0] else 1

def add_account():
    def add_account_thread():
        first_name = first_name_entry.get().strip()
        last_name = last_name_entry.get().strip()
        account_id = account_id_entry.get().strip()
        initial_balance = initial_balance_entry.get().strip()

        if not first_name or not last_name or not account_id or not initial_balance:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            initial_balance = float(initial_balance)
        except ValueError:
            messagebox.showerror("Error", "Invalid balance")
            return

        customer_id = get_next_customer_id()

        conn = sqlite3.connect('BankAccounts.db')
        c = conn.cursor()
        c.execute("INSERT INTO Customer (CustomerID, FirstName, LastName) VALUES (?, ?, ?)",
                  (customer_id, first_name, last_name))
        c.execute("INSERT INTO Account (AccountID, CustomerID, Balance) VALUES (?, ?, ?)",
                  (account_id, customer_id, initial_balance))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Account added successfully")
        print_balances()

    threading.Thread(target=add_account_thread).start()

def delete_account():
    def delete_account_thread():
        account_id = account_id_entry.get().strip()

        if not account_id:
            messagebox.showerror("Error", "Account ID is required")
            return

        conn = sqlite3.connect('BankAccounts.db')
        c = conn.cursor()
        c.execute("DELETE FROM Account WHERE AccountID = ?", (account_id,))
        c.execute("DELETE FROM Customer WHERE CustomerID NOT IN (SELECT CustomerID FROM Account)")
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Account deleted successfully")
        print_balances()

    threading.Thread(target=delete_account_thread).start()

# Existing functions...

window = tk.Tk()
window.title("Bank Transfer")
window.geometry("400x600")

# Create frames for better layout
input_frame = tk.Frame(window, padx=10, pady=10)
input_frame.pack(fill='x')

balance_frame = tk.Frame(window, padx=10, pady=10)
balance_frame.pack(fill='x')

button_frame = tk.Frame(window, padx=10, pady=10)
button_frame.pack(fill='x')

# Input fields
tk.Label(input_frame, text="Sender:").grid(row=0, column=0, sticky='w')
sender_entry = tk.Entry(input_frame)
sender_entry.grid(row=0, column=1, sticky='ew')

tk.Label(input_frame, text="Receiver:").grid(row=1, column=0, sticky='w')
receiver_entry = tk.Entry(input_frame)
receiver_entry.grid(row=1, column=1, sticky='ew')

tk.Label(input_frame, text="Amount:").grid(row=2, column=0, sticky='w')
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=2, column=1, sticky='ew')

# Balance display
balance_text = tk.Text(balance_frame, height=10, width=30)
balance_text.pack(fill='x')

# Buttons
transfer_button = tk.Button(button_frame, text="Transfer", command=lambda: window.after(0, transfer_money))
transfer_button.grid(row=0, column=0, padx=5, pady=5)

tk.Label(button_frame, text="Customer Name or ID:").grid(row=1, column=0, sticky='w')
customer_name_entry = tk.Entry(button_frame)
customer_name_entry.grid(row=1, column=1, sticky='ew')

show_balance_button = tk.Button(button_frame, text="Show Customer Balance", command=lambda: window.after(0, show_customer_balance))
show_balance_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Add account fields
tk.Label(button_frame, text="First Name:").grid(row=3, column=0, sticky='w')
first_name_entry = tk.Entry(button_frame)
first_name_entry.grid(row=3, column=1, sticky='ew')

tk.Label(button_frame, text="Last Name:").grid(row=4, column=0, sticky='w')
last_name_entry = tk.Entry(button_frame)
last_name_entry.grid(row=4, column=1, sticky='ew')

tk.Label(button_frame, text="Account ID:").grid(row=5, column=0, sticky='w')
account_id_entry = tk.Entry(button_frame)
account_id_entry.grid(row=5, column=1, sticky='ew')

tk.Label(button_frame, text="Initial Balance:").grid(row=6, column=0, sticky='w')
initial_balance_entry = tk.Entry(button_frame)
initial_balance_entry.grid(row=6, column=1, sticky='ew')

add_account_button = tk.Button(button_frame, text="Add Account", command=lambda: window.after(0, add_account))
add_account_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

delete_account_button = tk.Button(button_frame, text="Delete Account", command=lambda: window.after(0, delete_account))
delete_account_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Ensure the input and button frames expand with the window
input_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(1, weight=1)

window.mainloop()