import sqlite3
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from decimal import Decimal, InvalidOperation

db_path = 'Accounts.db'
MASTER_PIN = '1357'

# Check if the database already exists
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''CREATE TABLE Account
                 (Name text, AccountID int, Balance real, PIN text)''')
    c.execute("INSERT INTO Account VALUES ('jake', 1001, 35.14, '1234')")
    c.execute("INSERT INTO Account VALUES ('tim', 2002, 150.0, '5678')")
    c.execute("INSERT INTO Account VALUES ('john', 3003, 12.75, '9101')")

    # Save (commit) the changes
    conn.commit()
    conn.close()


def get_balance(name):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT Balance FROM Account WHERE Name = ?", (name,))
    result = c.fetchone()
    conn.close()
    return Decimal(result[0]) if result else None


def update_balance(name, amount):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("UPDATE Account SET Balance = ? WHERE Name = ?", (float(amount), name))
    conn.commit()
    conn.close()


def check_pin(name, entered_pin):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT PIN FROM Account WHERE Name = ?", (name,))
    result = c.fetchone()
    conn.close()
    return result[0] == entered_pin if result else False


def transfer_money():
    from_name = entry_from_name.get().lower()
    to_name = entry_to_name.get().lower()
    try:
        amount = Decimal(entry_amount.get())
    except InvalidOperation:
        messagebox.showerror("Error", "Invalid amount format.")
        return

    from_pin = entry_from_pin.get()
    if not check_pin(from_name, from_pin):
        messagebox.showerror("Error", "Incorrect PIN for the sender.")
        return

    from_balance = get_balance(from_name)
    to_balance = get_balance(to_name)

    if from_balance is None or to_balance is None:
        messagebox.showerror("Error", "One or both accounts not found.")
        return

    if from_balance < amount:
        messagebox.showerror("Error", "Insufficient funds.")
        return

    update_balance(from_name, from_balance - amount)
    update_balance(to_name, to_balance + amount)

    messagebox.showinfo("Success", "Transfer completed successfully.")
    display_balances()


def display_balances():
    name = entry_name.get().lower()
    entered_pin = entry_pin.get()

    if name == 'admin' and entered_pin == MASTER_PIN:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT Name, Balance FROM Account")
        balances = c.fetchall()
        conn.close()

        balance_text = "\n".join([f"{name}: £{Decimal(balance):.2f}" for name, balance in balances])
    else:
        if not check_pin(name, entered_pin):
            messagebox.showerror("Error", "Incorrect PIN.")
            return

        balance = get_balance(name)
        if balance is None:
            messagebox.showerror("Error", "Account not found.")
            return

        balance_text = f"{name}: £{balance:.2f}"

    label_balances.config(text=balance_text)


# noinspection PyTypeChecker
def main_screen():
    global entry_from_name, entry_to_name, entry_amount, entry_from_pin, entry_name, entry_pin, label_balances

    root = tk.Tk()
    root.title("ATM - Bank Account Transfer")
    root.geometry("400x300")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12))

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Button(frame, text="Show Balances", command=show_balance_screen).grid(row=0, column=0, pady=10)
    ttk.Button(frame, text="Transfer", command=transfer_screen).grid(row=0, column=1, pady=10)

    label_balances = ttk.Label(frame, text="", relief="sunken", padding="5")
    label_balances.grid(row=1, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    root.mainloop()


def show_balance_screen():
    global entry_name, entry_pin

    balance_screen = tk.Toplevel()
    balance_screen.title("Show Balance")
    balance_screen.geometry("300x200")
    balance_screen.resizable(False, False)

    ttk.Label(balance_screen, text="Customer Name:").pack(pady=5)
    entry_name = ttk.Entry(balance_screen)
    entry_name.pack(pady=5)

    ttk.Label(balance_screen, text="PIN:").pack(pady=5)
    entry_pin = ttk.Entry(balance_screen, show="*")
    entry_pin.pack(pady=5)

    ttk.Button(balance_screen, text="Submit", command=display_balances).pack(pady=10)


def transfer_screen():
    global entry_from_name, entry_to_name, entry_amount, entry_from_pin

    transfer_screen = tk.Toplevel()
    transfer_screen.title("Transfer Money")
    transfer_screen.geometry("400x300")
    transfer_screen.resizable(False, False)

    ttk.Label(transfer_screen, text="From Customer Name:").pack(pady=5)
    entry_from_name = ttk.Entry(transfer_screen)
    entry_from_name.pack(pady=5)

    ttk.Label(transfer_screen, text="From Customer PIN:").pack(pady=5)
    entry_from_pin = ttk.Entry(transfer_screen, show="*")
    entry_from_pin.pack(pady=5)

    ttk.Label(transfer_screen, text="To Customer Name:").pack(pady=5)
    entry_to_name = ttk.Entry(transfer_screen)
    entry_to_name.pack(pady=5)

    ttk.Label(transfer_screen, text="Amount to Transfer:").pack(pady=5)
    entry_amount = ttk.Entry(transfer_screen)
    entry_amount.pack(pady=5)

    ttk.Button(transfer_screen, text="Transfer", command=transfer_money).pack(pady=10)


main_screen()
