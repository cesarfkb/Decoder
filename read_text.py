import re
import tkinter as tk
from tkinter import filedialog, scrolledtext

def ler_texto(text: str):
    print(text)

def validar_texto(text: str):
    pattern = r'^[^0-2]*$|^[0-1]*$'
    if text.isnumeric() and bool(re.match(pattern, text)):
        return True

def load_file():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def submit_text():
    text_content = text_area.get(1.0, tk.END).strip()
    
    if validar_texto(text_content):
        ler_texto(text_content)

# Create the main application window
root = tk.Tk()
root.title("Text Input or File Loader")

# Create a text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
text_area.pack(padx=10, pady=10)

# Create buttons for loading a file and submitting text
load_button = tk.Button(root, text="Load Text File", command=load_file)
load_button.pack(side=tk.LEFT, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit Text", command=submit_text)
submit_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the application
root.mainloop()

