def translate_to_morse():
    text = input_text.get().upper()
    morse = ''
    for char in text:
        if char in morse_code:
            morse += morse_code[char] + ' '
        else:
            morse += char + ' '
    output_text.set(morse)

# Function to translate Morse code to text
def translate_to_text():
    morse = input_text.get()
    text = ''
    morse_code_inv = {v: k for k, v in morse_code.items()}  # Invert the morse_code dictionary for easier lookup
    for char in morse.split(' '):
        if char in morse_code_inv:
            text += morse_code_inv[char]
        elif char:  # If char is not empty and not in morse_code_inv, it's an error
            messagebox.showerror("Error", "Invalid Morse Code")
            return
    output_text.set(text)

# Clear both input and output fields
def clear_fields():
    input_text.delete(0, tk.END)
    output_text.set('')

# Copy output to clipboard
def copy_to_clipboard():
    pyperclip.copy(output_text.get())
    messagebox.showinfo("Copied", "Text copied to clipboard")

# Create the tkinter window
import tkinter as tk
from tkinter import messagebox
import pyperclip  # For clipboard operations, might need to install via pip

# Assuming morse_code dictionary is defined above this code

# Function to translate text to Morse code
def translate_to_morse():
    text = input_text.get().upper()
    morse = ''
    for char in text:
        if char in morse_code:
            morse += morse_code[char] + ' '
        else:
            morse += char + ' '
    output_text.set(morse)

# Function to translate Morse code to text
def translate_to_text():
    morse = input_text.get()
    text = ''
    morse_code_inv = {v: k for k, v in morse_code.items()}  # Invert the morse_code dictionary for easier lookup
    for char in morse.split(' '):
        if char in morse_code_inv:
            text += morse_code_inv[char]
        elif char:  # If char is not empty and not in morse_code_inv, it's an error
            messagebox.showerror("Error", "Invalid Morse Code")
            return
    output_text.set(text)

# Clear both input and output fields
def clear_fields():
    input_text.delete(0, tk.END)
    output_text.set('')

# Copy output to clipboard
def copy_to_clipboard():
    pyperclip.copy(output_text.get())
    messagebox.showinfo("Copied", "Text copied to clipboard")
