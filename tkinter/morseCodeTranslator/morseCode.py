import tkinter as tk
import morseFunctions as mf
# Define the Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    ' ': '|'
}

from tkinter import messagebox
import pyperclip

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

# Create the tkinter window
# Adjustments start from the creation of the tkinter window

window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("400x350")  # Adjusted window size for better layout

# Create a frame for input elements
input_frame = tk.Frame(window, padx=10, pady=10)
input_frame.pack(fill='x')

input_label = tk.Label(input_frame, text="Enter text or Morse code:")
input_label.grid(row=0, column=0, sticky='w')
input_text = tk.Entry(input_frame)
input_text.grid(row=1, column=0, sticky='ew')

# Create a frame for output elements
output_frame = tk.Frame(window, padx=10, pady=10)
output_frame.pack(fill='x')

output_label = tk.Label(output_frame, text="Translation:")
output_label.grid(row=0, column=0, sticky='w')
output_text = tk.StringVar()
output_entry = tk.Entry(output_frame, textvariable=output_text, state='readonly')
output_entry.grid(row=1, column=0, sticky='ew')

# Create a frame for buttons
buttons_frame = tk.Frame(window, padx=10, pady=10)
buttons_frame.pack(fill='x')

translate_to_morse_button = tk.Button(buttons_frame, text="Text to Morse", command=translate_to_morse)
translate_to_morse_button.grid(row=0, column=0, padx=5, pady=5)

translate_to_text_button = tk.Button(buttons_frame, text="Morse to Text", command=translate_to_text)
translate_to_text_button.grid(row=0, column=1, padx=5, pady=5)

clear_button = tk.Button(buttons_frame, text="Clear", command=clear_fields)
clear_button.grid(row=0, column=2, padx=5, pady=5)

copy_button = tk.Button(buttons_frame, text="Copy to Clipboard", command=mf.copy_to_clipboard)
copy_button.grid(row=0, column=3, padx=5, pady=5)

# Ensure the input and output entries expand with the window
input_frame.columnconfigure(0, weight=1)
output_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure((0, 1, 2, 3), weight=1)

from tkinter import filedialog  # Import required for opening the file dialog

# Function to save the translated text to a file
def save_to_file():
    # Open a file dialog to choose the file to save to
    filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:  # If no file is selected, return
        return
    with open(filepath, "w") as output_file:
        text = output_text.get()
        output_file.write(text)
    messagebox.showinfo("Saved", "The translated text has been saved.")

# Add the save button to the buttons_frame (assuming buttons_frame is already defined)
save_button = tk.Button(buttons_frame, text="Save to File", command=save_to_file)
save_button.grid(row=0, column=4, padx=5, pady=5)  # Adjust the column index based on your layout

# Ensure the buttons_frame column configuration is updated to include the new button
buttons_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)

window.mainloop()