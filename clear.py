import tkinter as tk
from tkinter import scrolledtext
import os

def clear_text():
    current_text = text_area.get("1.0", tk.END)
    cleaned_text = current_text.replace('"','')
    cleaned_text = cleaned_text.replace('”','')
    cleaned_text = cleaned_text.replace('“','')
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", cleaned_text)

def copy_text():
    text = text_area.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text)

def save_text():
    try:
        num = int(number_entry.get())
        filename = f"file_{num}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text_area.get("1.0", tk.END).strip())
        number_entry.delete(0, tk.END)
        number_entry.insert(0, str(num))
    except ValueError:
        pass  # Ignore if not a number

def next_save():
    try:
        num = int(number_entry.get())
        num += 1
        number_entry.delete(0, tk.END)
        number_entry.insert(0, str(num))
        filename = f"file_{num}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text_area.get("1.0", tk.END).strip())
    except ValueError:
        pass

root = tk.Tk()
root.title("Text Input GUI")
root.geometry("800x600")

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
text_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

number_label = tk.Label(input_frame, text="File Number:")
number_label.pack(side=tk.LEFT, padx=5)

number_entry = tk.Entry(input_frame, width=10)
number_entry.pack(side=tk.LEFT, padx=5)
number_entry.insert(0, "1")  # Default to 1

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(button_frame, text="Copy", command=copy_text)
copy_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(button_frame, text="Save", command=save_text)
save_button.pack(side=tk.LEFT, padx=10)

next_save_button = tk.Button(button_frame, text="Next Save", command=next_save)
next_save_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
