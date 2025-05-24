import tkinter as tk
from tkinter import ttk, messagebox
import winsound, time

# Morse dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', ' ': '/'
}

# Theme setup
themes = {
    "light": {"bg": "white", "fg": "black", "button": "#3498db", "hover": "#2980b9"},
    "dark": {"bg": "#2c3e50", "fg": "white", "button": "#e67e22", "hover": "#d35400"},
}
theme = "light"

# Convert text to Morse
def text_to_morse(text):
    return ' '.join(MORSE_CODE.get(c.upper(), '') for c in text)

# Play Morse audio
def play_morse(code):
    for char in code:
        if char == '.': winsound.Beep(1000, 200)
        elif char == '-': winsound.Beep(1000, 600)
        elif char == ' ': time.sleep(0.2)
        elif char == '/': time.sleep(0.5)

# Actions
def convert():
    text = entry.get()
    if not text:
        messagebox.showerror("Error", "Enter text first.")
        return
    morse = text_to_morse(text)
    output.config(text=morse)
    play_morse(morse)

def clear():
    entry.delete(0, tk.END)
    output.config(text="")

def copy():
    root.clipboard_clear()
    root.clipboard_append(output.cget("text"))
    messagebox.showinfo("Copied", "Morse code copied!")

def toggle_theme():
    global theme
    theme = "dark" if theme == "light" else "light"
    apply_theme()

def apply_theme():
    t = themes[theme]
    root.config(bg=t["bg"])
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Entry):
            widget.config(bg=t["bg"], fg=t["fg"])
    output.config(bg=t["bg"], fg=t["fg"])
    style.configure("TButton", background=t["button"], foreground="white")
    style.map("TButton", background=[("active", t["hover"])])

# UI Setup
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("500x400")

style = ttk.Style()
style.theme_use("default")

tk.Label(root, text="Enter text:").pack(pady=10)
entry = tk.Entry(root, font=("Segoe UI", 12), width=40)
entry.pack(pady=5)

ttk.Button(root, text="Convert & Play", command=convert).pack(pady=5)
ttk.Button(root, text="Clear", command=clear).pack(pady=5)
ttk.Button(root, text="Copy Morse", command=copy).pack(pady=5)
ttk.Button(root, text="Toggle Theme", command=toggle_theme).pack(pady=5)

output = tk.Label(root, text="", font=("Courier", 12), wraplength=450)
output.pack(pady=20)

apply_theme()
root.mainloop()
