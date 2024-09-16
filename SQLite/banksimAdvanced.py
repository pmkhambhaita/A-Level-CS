import sqlite3
import tkinter as tk
from tkinter import messagebox
from threading import Thread

def get_balance(customer_name):
    conn = sqlite3.connect('BankAccounts.db')
    c = conn.cursor()
    c.execute("SELECT Balance FROM Account WHERE CustomerName=?", (customer_name,))
    balance = c.fetchone()
    conn.close()
    return balance[0] if balance else None

def transfer_money():
    def task():
        sender = sender_entry.get()
        receiver = receiver_entry.get()
        try:
            amount = float(amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return

        if amount <= 0:
            messagebox.showerror("Error", "Transfer amount must be positive")
            return

        sender_balance = get_balance(sender)
        receiver_balance = get_balance(receiver)

        if sender_balance is None or receiver_balance is None:
            messagebox.showerror("Error", "One or both customers not found")
            return

        if sender_balance < amount:
            messagebox.showerror("Error", "Insufficient funds")
            return

        conn = sqlite3.connect('BankAccounts.db')
        c = conn.cursor()
        c.execute("UPDATE Account SET Balance = Balance - ? WHERE CustomerName = ?", (amount, sender))
        c.execute("UPDATE Account SET Balance = Balance + ? WHERE CustomerName = ?", (amount, receiver))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Transfer completed")
        print_balances()

    Thread(target=task).start()

def print_balances():
    def task():
        conn = sqlite3.connect('BankAccounts.db')
        c = conn.cursor()
        c.execute("SELECT CustomerName, Balance FROM Account")
        balances = c.fetchall()
        conn.close()

        balance_text.delete(1.0, tk.END)
        for account in balances:
            balance_text.insert(tk.END, f"{account[0]}: £{account[1]:.2f}\n")

    Thread(target=task).start()

def show_customer_balance():
    def task():
        customer_name = customer_name_entry.get()
        balance = get_balance(customer_name)
        if balance is not None:
            messagebox.showinfo("Balance", f"{customer_name}'s balance: £{balance:.2f}")
        else:
            messagebox.showerror("Error", "Customer not found")

    Thread(target=task).start()

window = tk.Tk()
window.title("Bank Transfer")
window.geometry("400x400")

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
transfer_button = tk.Button(button_frame, text="Transfer", command=transfer_money)
transfer_button.grid(row=0, column=0, padx=5, pady=5)

tk.Label(button_frame, text="Customer Name:").grid(row=1, column=0, sticky='w')
customer_name_entry = tk.Entry(button_frame)
customer_name_entry.grid(row=1, column=1, sticky='ew')

show_balance_button = tk.Button(button_frame, text="Show Customer Balance", command=show_customer_balance)
show_balance_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Ensure the input and button frames expand with the window
input_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(1, weight=1)

window.mainloop()