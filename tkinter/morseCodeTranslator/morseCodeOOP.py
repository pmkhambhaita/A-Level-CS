import tkinter as tk
from tkinter import filedialog, messagebox

class MorseCodeTranslator:
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
        '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }

    @staticmethod
    def to_morse(text):
        return ' '.join(MorseCodeTranslator.morse_code_dict.get(char.upper(), char) for char in text)

    @staticmethod
    def to_text(morse):
        morse_to_text_dict = {value: key for key, value in MorseCodeTranslator.morse_code_dict.items()}
        return ''.join(morse_to_text_dict.get(char, '') for char in morse.split(' '))

class MorseCodeApp:
    def __init__(self, master):
        self.master = master
        master.title("Morse Code Translator")

        # Input field
        self.input_text = tk.StringVar()
        self.input_entry = tk.Entry(master, textvariable=self.input_text)
        self.input_entry.pack()

        # Translate to Morse button
        self.translate_to_morse_button = tk.Button(master, text="Text to Morse", command=self.translate_to_morse)
        self.translate_to_morse_button.pack()

        # Translate to Text button
        self.translate_to_text_button = tk.Button(master, text="Morse to Text", command=self.translate_to_text)
        self.translate_to_text_button.pack()

        # Output field
        self.output_text = tk.StringVar()
        self.output_entry = tk.Entry(master, textvariable=self.output_text, state='readonly')
        self.output_entry.pack()

        # Load button
        self.load_button = tk.Button(master, text="Load Text File", command=self.load_from_file)
        self.load_button.pack()

        # Save button
        self.save_button = tk.Button(master, text="Save to File", command=self.save_to_file)
        self.save_button.pack()

    def translate_to_morse(self):
        text = self.input_text.get()
        morse = MorseCodeTranslator.to_morse(text)
        self.output_text.set(morse)

    def translate_to_text(self):
        morse = self.input_text.get()
        text = MorseCodeTranslator.to_text(morse)
        self.output_text.set(text)

    def load_from_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, "r") as input_file:
            text = input_file.read()
        self.input_text.set(text)

    def save_to_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.output_text.get()
            output_file.write(text)
        messagebox.showinfo("Saved", "The translated text has been saved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeApp(root)
    root.mainloop()