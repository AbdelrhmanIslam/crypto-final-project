import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label
from tkinter import Text
import string

S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
    0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
    0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
    0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
    0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
    0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
    0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
    0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
    0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
    0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
    0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
    0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
    0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
    0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
    0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
    0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
    0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16,
]

INV_S_BOX = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38,
    0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87,
    0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d,
    0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2,
    0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
    0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
    0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a,
    0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02,
    0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea,
    0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85,
    0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89,
    0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20,
    0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31,
    0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
    0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0,
    0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26,
    0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d,
]

# MixColumns
def xtime(a):
    return ((a << 1) ^ 0x1b) & 0xff if (a & 0x80) else a << 1

# GF(2^8)
def mul(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        high_bit_set = a & 0x80
        a = (a << 1) & 0xff
        if high_bit_set:
            a ^= 0x1b
        b >>= 1
    return p

# transform 16 bytes to 4x4 matrix
def to_matrix(text):
    return [list(text[i:i+4]) for i in range(0, 16, 4)]

# transform 4x4 matrix to 16 bytes
def from_matrix(matrix):
    return bytes(sum(matrix, []))

def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = S_BOX[state[i][j]]

def inv_sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = INV_S_BOX[state[i][j]]

def shift_rows(state):
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]

def inv_shift_rows(state):
    state[1] = state[1][-1:] + state[1][:-1]
    state[2] = state[2][-2:] + state[2][:-2]
    state[3] = state[3][-3:] + state[3][:-3]

def mix_columns(state):
    for i in range(4):
        s0 = state[0][i]
        s1 = state[1][i]
        s2 = state[2][i]
        s3 = state[3][i]

        state[0][i] = mul(s0, 2) ^ mul(s1, 3) ^ s2 ^ s3
        state[1][i] = s0 ^ mul(s1, 2) ^ mul(s2, 3) ^ s3
        state[2][i] = s0 ^ s1 ^ mul(s2, 2) ^ mul(s3, 3)
        state[3][i] = mul(s0, 3) ^ s1 ^ s2 ^ mul(s3, 2)

def inv_mix_columns(state):
    for i in range(4):
        s0 = state[0][i]
        s1 = state[1][i]
        s2 = state[2][i]
        s3 = state[3][i]

        state[0][i] = mul(s0, 0x0e) ^ mul(s1, 0x0b) ^ mul(s2, 0x0d) ^ mul(s3, 0x09)
        state[1][i] = mul(s0, 0x09) ^ mul(s1, 0x0e) ^ mul(s2, 0x0b) ^ mul(s3, 0x0d)
        state[2][i] = mul(s0, 0x0d) ^ mul(s1, 0x09) ^ mul(s2, 0x0e) ^ mul(s3, 0x0b)
        state[3][i] = mul(s0, 0x0b) ^ mul(s1, 0x0d) ^ mul(s2, 0x09) ^ mul(s3, 0x0e)

def add_round_key(state, key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= key[i][j]

# transform key to 4x4 matrix
def key_to_matrix(key):
    return [list(key[i:i+4]) for i in range(0, 16, 4)]

# block is 16 bytes 
def aes_encrypt(block, key):
    state = to_matrix(block)
    round_key = key_to_matrix(key)

    add_round_key(state, round_key)

    for _ in range(9):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, round_key)

    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, round_key)

    return from_matrix(state)

# block is 16 bytes
def aes_decrypt(block, key):
    state = to_matrix(block)
    round_key = key_to_matrix(key)

    add_round_key(state, round_key)
    for _ in range(9):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, round_key)
        inv_mix_columns(state)
    inv_shift_rows(state)
    inv_sub_bytes(state)
    add_round_key(state, round_key)

    return from_matrix(state)

def filter_text(text):
    allowed_chars = string.ascii_letters + string.digits + " "
    return "".join(c for c in text if c in allowed_chars)


#! GUI
class AESApp:
    def __init__(self, master):
        self.master = master
        master.title("AES Encryption Tool")
        style = Style(theme="darkly")
        self.master.geometry("600x600")

        self.label_key = Label(master, text="Enter AES Key (16 characters):")
        self.label_key.pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_key = Entry(master, width=50)
        self.entry_key.insert(0, "thisis16bytekey!")
        self.entry_key.pack(padx=10, pady=(0, 10))

        self.label_input = Label(master, text="Input Text (English letters and digits only):")
        self.label_input.pack(anchor="w", padx=10, pady=5)

        self.input_text = Text(master, height=5, width=70)
        self.input_text.pack(padx=10)
        self.input_text.bind("<KeyRelease>", self.validate_input)

        self.button_encrypt = Button(master, text="Encrypt", command=self.encrypt_text)
        self.button_encrypt.pack(pady=10)

        self.label_cipher = Label(master, text="Encrypted Output (Hex):")
        self.label_cipher.pack(anchor="w", padx=10)

        self.cipher_output = Text(master, height=5, width=70, state="disabled")
        self.cipher_output.pack(padx=10)

        self.button_decrypt = Button(master, text="Decrypt", command=self.decrypt_text)
        self.button_decrypt.pack(pady=10)

        self.label_decrypted = Label(master, text="Decrypted Output:")
        self.label_decrypted.pack(anchor="w", padx=10)

        self.decrypted_output = Text(master, height=5, width=70, state="disabled")
        self.decrypted_output.pack(padx=10)

        self.button_reset = Button(master, text="Reset All", command=self.reset_all)
        self.button_reset.pack(pady=10)
        
        self.label_manual_cipher = Label(master, text="Or Paste Ciphertext Here (Hex):")
        self.label_manual_cipher.pack(anchor="w", padx=10)

        self.manual_cipher_input = Text(master, height=5, width=70)
        self.manual_cipher_input.pack(padx=10, pady=(0, 10)) #TODO:FLAG

    def get_key(self):
        key = self.entry_key.get().strip().encode("utf-8")
        if len(key) != 16:
            raise ValueError("Key must be exactly 16 characters.")
        return key

    def validate_input(self, event=None):
        current = self.input_text.get("1.0", "end-1c")
        filtered = filter_text(current)
        if current != filtered:
            self.input_text.delete("1.0", "end")
            self.input_text.insert("1.0", filtered)

    def reset_all(self):#TODO:FLAG
       self.input_text.delete("1.0", "end")
       self.set_text(self.cipher_output, "")
       self.set_text(self.decrypted_output, "")
       self.manual_cipher_input.delete("1.0", "end")

    def set_text(self, widget, text):
        widget.config(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", text)
        widget.config(state="disabled")

    def pad(self, data):
        pad_len = 16 - (len(data) % 16)
        return data + bytes([pad_len] * pad_len)

    def unpad(self, data):
        pad_len = data[-1]
        if pad_len < 1 or pad_len > 16:
            raise ValueError("Invalid padding length.")
        return data[:-pad_len]

    def encrypt_text(self):
        plaintext = self.input_text.get("1.0", "end-1c").encode("utf-8")
        if not plaintext:
            messagebox.showwarning("Input Required", "Please enter text to encrypt.")
            return
        try:
            key = self.get_key()
        except ValueError as e:
            messagebox.showerror("Key Error", str(e))
            return

        padded = self.pad(plaintext)

        ciphertext = b""
        for i in range(0, len(padded), 16):
            block = padded[i:i+16]
            encrypted_block = aes_encrypt(block, key)
            ciphertext += encrypted_block

        self.set_text(self.cipher_output, ciphertext.hex().upper())
        self.set_text(self.decrypted_output, "")

    def decrypt_text(self): #TODO:FLAG
        manual_input = self.manual_cipher_input.get("1.0", "end-1c").strip()
        hex_cipher = manual_input if manual_input else self.cipher_output.get("1.0", "end-1c").strip()

        if not hex_cipher:
            messagebox.showwarning("No Ciphertext", "Please encrypt text first.")
            return
        try:
            key = self.get_key()
        except ValueError as e:
            messagebox.showerror("Key Error", str(e))
            return

        try:
            ciphertext = bytes.fromhex(hex_cipher)
        except ValueError:
            messagebox.showerror("Invalid Ciphertext", "Ciphertext is not valid hex.")
            return

        if len(ciphertext) % 16 != 0:
            messagebox.showerror("Invalid Ciphertext Length", "Ciphertext length must be multiple of 16 bytes.")
            return

        plaintext = b""
        try:
            for i in range(0, len(ciphertext), 16):
                block = ciphertext[i:i+16]
                decrypted_block = aes_decrypt(block, key)
                plaintext += decrypted_block
            plaintext = self.unpad(plaintext)
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))
            return

        self.set_text(self.decrypted_output, plaintext.decode("utf-8"))

if __name__ == "__main__":
    root = tk.Tk()
    app = AESApp(root)
    root.mainloop()