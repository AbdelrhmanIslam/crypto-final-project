🔐 Multi-layer Encryption/Decryption Tool


A powerful and interactive GUI tool for encrypting and decrypting text using multiple classical cryptographic algorithms, with support for applying several layers of encryption/decryption in sequence.

🚀 Features

Multiple classical algorithms:

Caesar Cipher
Playfair Cipher
Vigenère Cipher
Columnar Transposition (Row-Column)
Monoalphabetic Cipher
Rail Fence Cipher (Zigzag)


Multi-layer encryption/decryption.

Material-style modern GUI with ttkbootstrap.

Step-by-step result explanation.

Supports English input only for cleaner processing.



🖼️ Interface Preview




🧠 How to Use

Enter the input text.
Choose the operation (Encrypt or Decrypt).
Select an algorithm and provide a valid key.
Click ➕ Add Layer to queue the operation.
Add more layers as needed.
Click 🚀 Execute to process all layers.
Output with detailed steps will appear below.


🔑 Key Rules



Algorithm
Key Type



Caesar
Numeric


Zigzag (Railfence)
Numeric


Row Column
Sequence of digits (e.g., 312)


Playfair
Alphabetic


Vigenère
Alphabetic


Monoalphabetic
No key (auto-generated)



🛠️ Requirements

Python 3.7+
ttkbootstrap

Install it via:
pip install ttkbootstrap


📂 Additional Files Description
main.py
This file serves as the entry point for the application, providing a main menu to navigate between different encryption tools. It uses ttkbootstrap for a consistent, modern GUI. Key features include:

Main Menu:
A simple interface with buttons to launch the SDES tool, the multi-layer encryption tool (final_project.py), or exit the application.
Placeholder functionality for additional tools (displays a "Coming Soon" popup).


Functionality:
Launches SDES.py or final_project.py using subprocess.Popen to run them as separate processes.
Uses a customizable theme (darkly by default) for a cohesive look.



SDES.py
This file implements a Simplified Data Encryption Standard (S-DES) tool with a GUI built using tkinter. It focuses on binary encryption/decryption with an 8-bit block size and a 10-bit key. Key features include:

Algorithm:
Implements S-DES with initial permutation, two rounds of encryption/decryption using subkeys (K1, K2), and inverse permutation.
Supports key input as a 10-bit binary string, hexadecimal, or text (converted to binary).
Uses S-boxes (S0, S1) for substitution and permutation tables (P10, P8, EP, P4) for key generation and processing.


GUI Components:
Input fields for plaintext/ciphertext and a 10-bit key.
Dropdown to select the operation (Encrypt/Decrypt).
Buttons to run the operation or reset the interface.
Text area to display the binary output and detailed step-by-step log (e.g., initial permutation, round results, swap, final output).


Functionality:
Converts text input to binary and validates key input.
Displays detailed logs of the S-DES process for educational purposes.
Handles errors (e.g., invalid key length) with message boxes.
