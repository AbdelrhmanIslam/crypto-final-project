import tkinter as tk
from tkinter import messagebox, ttk

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def key_to_binary(key):
    key = key.strip()

    if all(c in '01' for c in key):
        if len(key) == 10:
            return key
        else:
            raise ValueError("The key must be exactly 10 bits long.")

    try:
        bin_key = bin(int(key, 16))[2:].zfill(10)
        if len(bin_key) == 10:
            return bin_key
        else:
            raise ValueError("The hexadecimal key must be 10 bits after conversion.")
    except:
        pass

    bin_key = ''.join(format(ord(char), '08b') for char in key)
    
    if len(bin_key) > 10:
        return bin_key[:10]
    
    if len(bin_key) < 10:
        return bin_key.zfill(10)
    
    return bin_key

    bin_key = ''.join(format(ord(char), '08b') for char in key)
    if len(bin_key) == 10:
        return bin_key

    raise ValueError("Key must be exactly 10 bits after conversion.")


def apply_permutation(data, table):
    return ''.join(data[i-1] for i in table)

def initial_permutation(data):
    return apply_permutation(data, [2, 6, 3, 1, 4, 8, 5, 7])

def inverse_permutation(data):
    return apply_permutation(data, [4, 1, 3, 5, 7, 2, 8, 6])

def left_shift(bits):
    return bits[1:] + bits[0]

def generate_keys(key):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    key = apply_permutation(key, P10)
    left, right = key[:5], key[5:]
    left = left_shift(left)
    right = left_shift(right)
    K1 = apply_permutation(left + right, P8)
    left = left_shift(left)
    right = left_shift(right)
    K2 = apply_permutation(left + right, P8)
    return K1, K2

def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

def s_box(input_bits, box):
    row = int(input_bits[0] + input_bits[3], 2)
    col = int(input_bits[1] + input_bits[2], 2)
    return format(box[row][col], '02b')

def fk(bits, key):
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    P4 = [2, 4, 3, 1]
    left, right = bits[:4], bits[4:]
    right_expanded = apply_permutation(right, EP)
    xored = xor(right_expanded, key)
    s0_res = s_box(xored[:4], S0)
    s1_res = s_box(xored[4:], S1)
    combined = apply_permutation(s0_res + s1_res, P4)
    return xor(left, combined) + right

def encrypt(plaintext, key):
    K1, K2 = generate_keys(key)
    log = ""
    bits = initial_permutation(plaintext)
    log += f"IP: {bits}\n"
    bits = fk(bits, K1)
    log += f"After Round 1: {bits}\n"
    bits = bits[4:] + bits[:4]
    log += f"Swap: {bits}\n"
    bits = fk(bits, K2)
    log += f"After Round 2: {bits}\n"
    bits = inverse_permutation(bits)
    log += f"Final: {bits}\n"
    return bits, log

def decrypt(ciphertext, key):
    K1, K2 = generate_keys(key)
    log = ""
    bits = initial_permutation(ciphertext)
    log += f"IP: {bits}\n"
    bits = fk(bits, K2)
    log += f"After Round 1: {bits}\n"
    bits = bits[4:] + bits[:4]
    log += f"Swap: {bits}\n"
    bits = fk(bits, K1)
    log += f"After Round 2: {bits}\n"
    bits = inverse_permutation(bits)
    log += f"Final: {bits}\n"
    return bits, log

def run_operation():
    result_display.config(state="normal")
    result_display.delete("1.0", tk.END)
    try:
        pt = plaintext_entry.get().strip()
        key = key_entry.get().strip()
        mode = operation_combo.get()

        binary_plaintext = text_to_binary(pt)

        key_bin = key_to_binary(key)

        if mode == "Encrypt":
            result, log = encrypt(binary_plaintext, key_bin)
            result_display.insert(tk.END, f"Encrypted: {result}\n\n{log}")
        else:
            result, log = decrypt(binary_plaintext, key_bin)
            result_display.insert(tk.END, f"Decrypted: {result}\n\n{log}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    result_display.config(state="disabled")

def reset_all():
    plaintext_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    operation_combo.set("Encrypt")
    result_display.config(state="normal")
    result_display.delete("1.0", tk.END)
    result_display.config(state="disabled")

S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,2,0]]
S1 = [[0,1,2,3],[3,0,1,2],[2,1,3,0],[1,3,0,2]]

root = tk.Tk()
root.title("Mini DES Tool")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

tk.Label(root, text="Enter Plaintext:", bg="#f0f8ff", font=("Arial", 12)).pack()
plaintext_entry = tk.Entry(root, font=("Arial", 12))
plaintext_entry.pack()

tk.Label(root, text="Enter 10-bit Key / Hex / Text:", bg="#f0f8ff", font=("Arial", 12)).pack()
key_entry = tk.Entry(root, font=("Arial", 12))
key_entry.pack()

tk.Label(root, text="Select Operation:", bg="#f0f8ff", font=("Arial", 12)).pack()
operation_combo = ttk.Combobox(root, values=["Encrypt", "Decrypt"], state="readonly")
operation_combo.set("Encrypt")
operation_combo.pack()

tk.Button(root, text="Run", command=run_operation, bg="#007acc", fg="white", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Reset", command=reset_all, bg="#cc0000", fg="white", font=("Arial", 12)).pack()

result_display = tk.Text(root, height=15, width=55, font=("Courier", 10), bg="#ffffff", fg="#000000")
result_display.pack(pady=10)
result_display.config(state="disabled")

root.mainloop()