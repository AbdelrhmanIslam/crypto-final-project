import tkinter as tk
from tkinter import ttk, messagebox
import string
import random
import math
import re
import ttkbootstrap as ttk

#! ===================== ALGORITHMS =====================

def caesar_encrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + int(key)) % 26
            result += chr(ord('a') + shift)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -int(key))

def playfair_encrypt(text, key):
    def create_matrix(key):
        key = ''.join(sorted(set(key), key=key.index))
        alphabet = 'abcdefghiklmnopqrstuvwxyz'
        matrix = [c for c in key if c in alphabet]
        for c in alphabet:
            if c not in matrix:
                matrix.append(c)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def process_text(text):
        text = text.replace('j', 'i')
        processed = ''
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else 'x'
            if a == b:
                processed += a + 'x'
                i += 1
            else:
                processed += a + b
                i += 2
        if len(processed) % 2 != 0:
            processed += 'x'
        return processed

    def find_coords(matrix, char):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char:
                    return r, c

    matrix = create_matrix(key.lower())
    text = ''.join([c for c in text.lower() if c.isalpha()])
    text = process_text(text)
    result = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        ra, ca = find_coords(matrix, a)
        rb, cb = find_coords(matrix, b)
        if ra == rb:
            result += matrix[ra][(ca+1)%5] + matrix[rb][(cb+1)%5]
        elif ca == cb:
            result += matrix[(ra+1)%5][ca] + matrix[(rb+1)%5][cb]
        else:
            result += matrix[ra][cb] + matrix[rb][ca]
    return result

def playfair_decrypt(text, key):
    def create_matrix(key):
        key = ''.join(sorted(set(key), key=key.index))
        alphabet = 'abcdefghiklmnopqrstuvwxyz'
        matrix = [c for c in key if c in alphabet]
        for c in alphabet:
            if c not in matrix:
                matrix.append(c)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_coords(matrix, char):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char:
                    return r, c

    matrix = create_matrix(key.lower())
    result = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        ra, ca = find_coords(matrix, a)
        rb, cb = find_coords(matrix, b)
        if ra == rb:
            result += matrix[ra][(ca-1)%5] + matrix[rb][(cb-1)%5]
        elif ca == cb:
            result += matrix[(ra-1)%5][ca] + matrix[(rb-1)%5][cb]
        else:
            result += matrix[ra][cb] + matrix[rb][ca]
    return result

def vigenere_encrypt(text, key):
    result = ''
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ''
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    return result

def columnar_encrypt(text, key):
    key = [int(k) for k in key]
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    
    padded = text.ljust(num_rows * num_cols, ' ')
    matrix = [padded[i:i+num_cols] for i in range(0, len(padded), num_cols)]
    
    ordered_matrix = ['' for _ in range(num_cols)]
    for i, col_idx in enumerate(sorted(range(num_cols), key=lambda x: key[x])):
        ordered_matrix[col_idx] = ''.join([row[i] for row in matrix])
    
    result = ''.join(ordered_matrix) 
    return result

def columnar_decrypt(text, key):
    key = [int(k) for k in key]
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    total_len = len(text)

    order = sorted(range(len(key)), key=lambda x: key[x])

    col_lengths = [num_rows] * num_cols
    for i in range(num_cols * num_rows - total_len):
        col_lengths[order[-(i+1)]] -= 1 

    cols = []
    idx = 0
    for length in col_lengths:
        cols.append(text[idx:idx+length])
        idx += length

    arranged_cols = [''] * num_cols
    for i, col_index in enumerate(order):
        arranged_cols[col_index] = cols[i]

    result = ''
    for i in range(num_rows):
        for col in arranged_cols:
            if i < len(col):
                result += col[i]

    return result.strip()

def monoalphabetic_encrypt(text):
    alphabet = string.ascii_lowercase
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    key = dict(zip(alphabet, shuffled))
    result = ''.join(key.get(c, c) for c in text.lower())
    return result, key

def monoalphabetic_decrypt(text, key):
    inverse = {v: k for k, v in key.items()}
    return ''.join(inverse.get(c, c) for c in text.lower())

def railfence_encrypt(text, key):
    rails = [''] * key
    down = False
    row = 0
    for char in text:
        rails[row] += char
        if row == 0 or row == key - 1:
            down = not down
        row += 1 if down else -1
    return ''.join(rails)

def railfence_decrypt(cipher, key):
    pattern = [['' for _ in range(len(cipher))] for _ in range(key)]
    idx = 0
    down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            down = True
        elif row == key - 1:
            down = False
        pattern[row][col] = '*'
        col += 1
        row += 1 if down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if pattern[i][j] == '*' and index < len(cipher):
                pattern[i][j] = cipher[index]
                index += 1

    result = ''
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            down = True
        elif row == key - 1:
            down = False
        result += pattern[row][col]
        col += 1
        row += 1 if down else -1
    return result


#? ============ GUI ============

app = ttk.Window(themename="darkly")  # Material design theme
app.title("Multi-layer Encryption/Decryption Tool")
app.geometry("720x700")

main_frame = ttk.Frame(app)
main_frame.pack(pady=20)

ttk.Label(main_frame, text="🔐 Input Text:").grid(row=0, column=0, sticky="w")
input_text = tk.Text(main_frame, height=5, width=80, bg="#2e2e2e", fg="#ffffff", insertbackground="white", wrap="word")
input_text.grid(row=1, column=0, columnspan=3, pady=5)

operation = ttk.Combobox(main_frame, values=["Encrypt", "Decrypt"], width=20, bootstyle="info")
operation.set("Encrypt")
operation.grid(row=2, column=0, pady=5)

algorithm = ttk.Combobox(main_frame, values=["Caesar", "Playfair", "Vigenère", "Row Column", "Monoalphabetic", "Zigzag"], width=20, bootstyle="primary")
algorithm.set("Caesar")
algorithm.grid(row=2, column=1, pady=5)

key_entry = ttk.Entry(main_frame, width=20, bootstyle="dark")
key_entry.grid(row=2, column=2, pady=5)

layers = []
layer_listbox = tk.Listbox(main_frame, width=90, bg="#2e2e2e", fg="#ffffff")
layer_listbox.grid(row=3, column=0, columnspan=3, pady=5)

def update_key_entry(*args):
    selected_algo = algorithm.get()
    if selected_algo == "Monoalphabetic":
        key_entry.delete(0, tk.END)
        key_entry.insert(0, "auto")
        key_entry.config(state="disabled")
    else:
        key_entry.config(state="normal")
        key_entry.delete(0, tk.END)

algorithm.bind("<<ComboboxSelected>>", update_key_entry)

def is_english(text):
    return re.fullmatch(r'[a-zA-Z ]*', text) is not None

def add_layer():
    algo = algorithm.get()
    op = operation.get()
    key = key_entry.get().strip()

    if algo == "Monoalphabetic":
        key = ''
    elif not key:
        messagebox.showerror("Error", "Key is required for this algorithm.")
        return
    elif algo in ["Caesar", "Zigzag", "Row Column"] and not key.isdigit():
        messagebox.showerror("Error", f"{algo} key must be a number.")
        return
    elif algo in ["Playfair", "Vigenère"] and not key.isalpha():
        messagebox.showerror("Error", f"{algo} key must contain only letters.")
        return

    layers.append((op, algo, key))
    layer_listbox.insert(tk.END, f"{op} {algo} | Key: {key if key else '[auto]'}")
    messagebox.showinfo("Layer Added", f"{op} {algo} added.")

def clean_text(text):
    return ''.join(c.lower() for c in text if c.isalpha() or c.isspace())

def execute():
    raw_text = input_text.get("1.0", tk.END).strip()
    text = clean_text(raw_text)

    if not is_english(text):
        messagebox.showerror("Error", "Only English letters are allowed.")
        return

    steps = ""
    current_text = text
    mono_key = None

    for i, (op, algo, key) in enumerate(layers):
        steps += f"\n🔹 Step {i+1}: {op} {algo}\n"
        steps += f"🔑 Key: {key if algo != 'Monoalphabetic' else '[auto]'}\n"
        steps += f"Input: {current_text}\n"

        if op == "Encrypt":
            if algo == "Caesar":
                current_text = caesar_encrypt(current_text, key)
            elif algo == "Playfair":
                current_text = playfair_encrypt(current_text, key)
            elif algo == "Vigenère":
                current_text = vigenere_encrypt(current_text, key)
            elif algo == "Row Column":
                current_text = columnar_encrypt(current_text, key)
            elif algo == "Monoalphabetic":
                current_text, mono_key = monoalphabetic_encrypt(current_text)
                steps += "🔑 Mono Key Map:\n"
                steps += f"{mono_key}\n"

            elif algo == "Zigzag":
                current_text = railfence_encrypt(current_text, int(key))
        else:
            if algo == "Caesar":
                current_text = caesar_decrypt(current_text, key)
            elif algo == "Playfair":
                current_text = playfair_decrypt(current_text, key)
            elif algo == "Vigenère":
                current_text = vigenere_decrypt(current_text, key)
            elif algo == "Row Column":
                current_text = columnar_decrypt(current_text, key)
            elif algo == "Monoalphabetic":
                if mono_key:
                    current_text = monoalphabetic_decrypt(current_text, mono_key)
                else:
                    messagebox.showerror("Error", "Mono key not available.")
                    return
            elif algo == "Zigzag":
                current_text = railfence_decrypt(current_text, int(key))

        steps += f"Output: {current_text}\n"

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, steps.strip())
    output_text.config(state="disabled")

def reset():
    input_text.delete("1.0", tk.END)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")
    layer_listbox.delete(0, tk.END)
    layers.clear()
    key_entry.config(state="normal")
    key_entry.delete(0, tk.END)

ttk.Button(main_frame, text="➕ Add Layer", command=add_layer).grid(row=4, column=0, pady=10)
ttk.Button(main_frame, text="🚀 Execute", command=execute).grid(row=4, column=1, pady=10)
ttk.Button(main_frame, text="🔄 Reset", command=reset).grid(row=4, column=2, pady=10)

output_text = tk.Text(app, height=12, width=80, bg="#2e2e2e", fg="#ffffff", wrap="word", state="disabled")
output_text.pack(pady=20)

app.mainloop()