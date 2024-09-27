import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
import re


def clean_currency_input(value):
    return re.sub(r'[^\d.]', '', value)


def get_customer_id(name):
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("SELECT CustomerID FROM Customer WHERE LOWER(FirstName || ' ' || LastName) = ?", (name.lower(),))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def get_balance_by_id(customer_id):
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("SELECT Balance FROM Account WHERE CustomerID = ?", (customer_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def transfer_money():
    sender_input = sender_entry.get().lower()
    receiver_input = receiver_entry.get().lower()
    amount_input = clean_currency_input(amount_entry.get())

    try:
        amount = float(amount_input)
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

    if sender_id == receiver_id:
        messagebox.showerror("Error", "Sender and receiver cannot be the same customer")
        return

    sender_balance = get_balance_by_id(sender_id)
    if sender_balance is None or sender_balance < amount:
        messagebox.showerror("Error", "Insufficient funds")
        return

    def transfer():
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

    prompt_pin_verification(sender_id, transfer)


def prompt_delete_account():
    def on_submit():
        account_id = account_id_entry.get().strip()
        if account_id:
            delete_account(account_id)
        delete_window.destroy()

    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Account")
    delete_window.geometry("300x150")

    tk.Label(delete_window, text="Account ID:").pack(pady=10)
    account_id_entry = tk.Entry(delete_window)
    account_id_entry.pack(pady=5)

    submit_button = tk.Button(delete_window, text="Delete", command=on_submit, bg="red", fg="white")
    submit_button.pack(pady=10)


def delete_account(account_id):
    def delete_account_thread():
        if not account_id:
            messagebox.showerror("Error", "Account ID is required")
            return

        conn = sqlite3.connect('BankAccounts.db')
        c = conn.cursor()
        c.execute("SELECT CustomerID FROM Account WHERE AccountID = ?", (account_id,))
        result = c.fetchone()
        conn.close()

        if result:
            customer_id = result[0]

            def delete():
                conn = sqlite3.connect('BankAccounts.db')
                c = conn.cursor()
                c.execute("DELETE FROM Account WHERE AccountID = ?", (account_id,))
                c.execute("DELETE FROM Customer WHERE CustomerID NOT IN (SELECT CustomerID FROM Account)")
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Account deleted successfully")
                print_balances()

            prompt_pin_verification(customer_id, delete)
        else:
            messagebox.showerror("Error", "Account ID does not exist")

    threading.Thread(target=delete_account_thread).start()


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
    else:
        try:
            first_name, last_name = input_value.split()
            customer_id = get_customer_id(f"{first_name} {last_name}")
        except ValueError:
            messagebox.showerror("Error", "Please enter both first and last names")
            return

    if customer_id is None:
        messagebox.showerror("Error", "Customer not found")
        return

    def show_balance():
        balance = get_balance_by_id(customer_id)
        if balance is not None:
            messagebox.showinfo("Balance", f"Customer ID {customer_id}'s balance: £{balance:.2f}")
        else:
            messagebox.showerror("Error", "Customer not found")

    # Only prompt for PIN if the customer exists
    if customer_id is not None:
        prompt_pin_verification(customer_id, show_balance)


def get_next_customer_id():
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("SELECT MAX(CustomerID) FROM Customer")
    result = c.fetchone()
    conn.close()
    return result[0] + 1 if result[0] else 1


def account_id_exists(account_id):
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("SELECT 1 FROM Account WHERE AccountID = ?", (account_id,))
    exists = c.fetchone() is not None
    conn.close()
    return exists


def add_account():
    def add_account_thread():
        first_name = first_name_entry.get().strip()
        last_name = last_name_entry.get().strip()
        account_id = account_id_entry.get().strip()
        initial_balance = initial_balance_entry.get().strip()
        pin = pin_entry.get().strip()

        if not first_name or not last_name or not account_id or not initial_balance or not pin:
            messagebox.showerror("Error", "All fields are required")
            return

        if account_id_exists(account_id):
            messagebox.showerror("Error", "Account ID already exists")
            return

        try:
            initial_balance = float(initial_balance)
        except ValueError:
            messagebox.showerror("Error", "Invalid balance")
            return

        customer_id = get_next_customer_id()

        conn = sqlite3.connect('BankAccounts.db')
        c = conn.cursor()
        c.execute("INSERT INTO Customer (CustomerID, FirstName, LastName, PIN) VALUES (?, ?, ?, ?)",
                  (customer_id, first_name, last_name, pin))
        c.execute("INSERT INTO Account (AccountID, CustomerID, Balance) VALUES (?, ?, ?)",
                  (account_id, customer_id, initial_balance))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Account added successfully")
        print_balances()

    threading.Thread(target=add_account_thread).start()


def verify_pin(customer_id, pin):
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("SELECT PIN FROM Customer WHERE CustomerID = ?", (customer_id,))
    result = c.fetchone()
    conn.close()
    return result[0] == pin if result else False


def prompt_pin_verification(customer_id, callback):
    def on_submit():
        pin = pin_entry.get().strip()
        if verify_pin(customer_id, pin):
            callback()
            pin_window.destroy()
        else:
            messagebox.showerror("Error", "Invalid PIN")

    pin_window = tk.Toplevel(window)
    pin_window.title("Enter PIN")
    pin_window.geometry("300x150")

    tk.Label(pin_window, text="PIN:").pack(pady=10)
    pin_entry = tk.Entry(pin_window, show="*")
    pin_entry.pack(pady=5)

    submit_button = tk.Button(pin_window, text="Submit", command=on_submit)
    submit_button.pack(pady=10)


window = tk.Tk()
window.title("Bank Transfer")
window.geometry("400x700")

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

# Transfer button
transfer_button = tk.Button(input_frame, text="Transfer", command=lambda: window.after(0, transfer_money))
transfer_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Divider
ttk.Separator(input_frame, orient='horizontal').grid(row=4, columnspan=2, sticky='ew', pady=10)

# Balance display
balance_text = tk.Text(balance_frame, height=10, width=30)
balance_text.pack(fill='x')

# Divider
ttk.Separator(balance_frame, orient='horizontal').pack(fill='x', pady=10)

# Buttons
tk.Label(button_frame, text="Customer Name or ID:").grid(row=0, column=0, sticky='w')
customer_name_entry = tk.Entry(button_frame)
customer_name_entry.grid(row=0, column=1, sticky='ew')

show_balance_button = tk.Button(button_frame, text="Show Customer Balance",
                                command=lambda: window.after(0, show_customer_balance))
show_balance_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Divider
ttk.Separator(button_frame, orient='horizontal').grid(row=2, columnspan=2, sticky='ew', pady=10)

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

tk.Label(button_frame, text="PIN:").grid(row=7, column=0, sticky='w')
pin_entry = tk.Entry(button_frame, show="*")
pin_entry.grid(row=7, column=1, sticky='ew')

add_account_button = tk.Button(button_frame, text="Add Account", command=lambda: window.after(0, add_account))
add_account_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Divider
ttk.Separator(button_frame, orient='horizontal').grid(row=9, columnspan=2, sticky='ew', pady=10)

delete_account_button = tk.Button(button_frame, text="Delete Account",
                                  command=lambda: window.after(0, prompt_delete_account), bg="red", fg="white")
delete_account_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

# Divider
ttk.Separator(button_frame, orient='horizontal').grid(row=11, columnspan=2, sticky='ew', pady=10)

# Test button to display all account balances
test_button = tk.Button(button_frame, text="Display All Account Balances (TEST ONLY)",
                        command=lambda: window.after(0, print_balances))
test_button.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

# Ensure the input and button frames expand with the window
input_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(1, weight=1)

window.mainloop()
