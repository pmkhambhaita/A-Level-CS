import tkinter as tk
# Define the Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    ' ': '|'
}

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
    for char in morse.split(' '):
        for key, value in morse_code.items():
            if char == value:
                text += key
    output_text.set(text)

# Create the tkinter window
window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("400x200")
window.configure(bg='white')

# Create the input label and entry
input_label = tk.Label(window, text="Enter text:")
input_label.pack()
input_text = tk.Entry(window)
input_text.pack()

# Create the translate to morse button
translate_to_morse_button = tk.Button(window, text="Translate to morse", command=translate_to_morse)
translate_to_morse_button.pack()

# Create the translate to text button

translate_to_text_button = tk.Button(window, text="Translate to text", command=translate_to_text)
translate_to_text_button.pack()

# Create the output label and entry
output_label = tk.Label(window, text="Morse code:")
output_label.pack()
output_text = tk.StringVar()
output_entry = tk.Entry(window, textvariable=output_text, state='readonly')
output_entry.pack()

# Run the tkinter event loop
window.mainloop()