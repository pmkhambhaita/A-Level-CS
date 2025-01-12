from tkinter import *
import tkinter as tk
import re

root = tk.Tk()
root.title("Login")
root.geometry("700x300")

# Create a frame to hold the grid
frame = Frame(root)
frame.pack()

selected_option = StringVar()
selected_option.set("student")  # Default value

# Create radio buttons
student_rb = Radiobutton(frame, text="Student", variable=selected_option, value="student")
student_rb.grid(row=0, column=0, padx=5, pady=5)

admin_rb = Radiobutton(frame, text="Admin", variable=selected_option, value="admin")
admin_rb.grid(row=0, column=1, padx=5, pady=5)

teacher_rb = Radiobutton(frame, text="Teacher", variable=selected_option, value="teacher")
teacher_rb.grid(row=0, column=2, padx=5, pady=5)


# Create labels and entries for username and password
username_label = Label(frame, text="Username:")
username_label.grid(row=1, column=0, padx=5, pady=5)
username_entry = Entry(frame)
username_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = Label(frame, text="Password:")
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry = Entry(frame, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Presence check for username and password
    if not username or not password:
        details.config(text="Username and password are required!", fg="red")
        return
    
    # Format check for username (simple email validation)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
        details.config(text="Invalid email format for username.", fg="red")
        return
    allowed_domains = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com", "aol.com", "protonmail.com", "icloud.com", "zoho.com", "yandex.com", "mail.com", "nobel.herts.sch.uk"]
    domain = username.split('@')[-1]  # Extract the domain from the email
    if domain not in allowed_domains:
        details.config(text="Email domain is not allowed.", fg="red")
        return

    # Adjusted excerpt from your provided code snippet
    # Password checks with levels
    missing_elements = []
    level = check_level.get()

    if level >= 2:
        if not re.search(r"[A-Z]", password):
            missing_elements.append("capital letter")
    if level >= 3:
        if not re.search(r"[0-9]", password):
            missing_elements.append("number")
    if level == 4:
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            missing_elements.append("special character")
    if not re.search(r"[a-z]", password):  # Always check for lowercase
        missing_elements.append("lowercase letter")

    if missing_elements:
        details.config(text=f"Password must include: {', '.join(missing_elements)}.", fg="red")
        return

    # Username checks based on user type
    user_type = selected_option.get()
    if user_type == "student":
        if not re.match(r"\d{2}[a-zA-Z]+[MECT]", username):
            details.config(text="Invalid student username format.", fg="red")
            return
    elif user_type == "teacher":
        if not re.match(r"[a-zA-Z]+\.[a-zA-Z]+", username):
            details.config(text="Invalid teacher username format.", fg="red")
            return
    elif user_type == "admin":
        if username != "admin":
            details.config(text="Invalid admin username.", fg="red")
            return
    print(f"Username: {username}, Password: {password}")
    details.config(text=f"Login successful for {username}.", fg="green")


details = Label(frame, text="")
details.grid(row=3, column=0, columnspan=2)


login_button = Button(frame, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


check_level = Scale(frame, from_=1, to=4, orient=HORIZONTAL, label="Check Level")
check_level.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

root.mainloop()