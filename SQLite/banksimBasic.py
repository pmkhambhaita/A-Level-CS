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
        amount = float(amount_entry.get())

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
            balance_text.insert(tk.END, f"{account[0]}: ${account[1]:.2f}\n")

    Thread(target=task).start()


def show_customer_balance():
    def task():
        customer_name = customer_name_entry.get()
        balance = get_balance(customer_name)
        if balance is not None:
            messagebox.showinfo("Balance", f"{customer_name}'s balance: ${balance:.2f}")
        else:
            messagebox.showerror("Error", "Customer not found")

    Thread(target=task).start()


window = tk.Tk()
window.title("Bank Transfer")

tk.Label(window, text="Sender:").grid(row=0, column=0)
sender_entry = tk.Entry(window)
sender_entry.grid(row=0, column=1)

tk.Label(window, text="Receiver:").grid(row=1, column=0)
receiver_entry = tk.Entry(window)
receiver_entry.grid(row=1, column=1)

tk.Label(window, text="Amount:").grid(row=2, column=0)
amount_entry = tk.Entry(window)
amount_entry.grid(row=2, column=1)

transfer_button = tk.Button(window, text="Transfer", command=transfer_money)
transfer_button.grid(row=3, column=0, columnspan=2)

balance_text = tk.Text(window, height=10, width=30)
balance_text.grid(row=4, column=0, columnspan=2)


tk.Label(window, text="Customer Name:").grid(row=6, column=0)
customer_name_entry = tk.Entry(window)
customer_name_entry.grid(row=6, column=1)

show_balance_button = tk.Button(window, text="Show Customer Balance", command=show_customer_balance)
show_balance_button.grid(row=8, column=0, columnspan=2)


window.mainloop()