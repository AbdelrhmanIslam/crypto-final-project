# 🔐 Multi-layer Encryption/Decryption Tool

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GUI: ttkbootstrap](https://img.shields.io/badge/GUI-ttkbootstrap-blueviolet?style=for-the-badge)](https://ttkbootstrap.readthedocs.io/)
![License: Educational](https://img.shields.io/badge/License-Educational-lightgrey?style=for-the-badge)
![Status: Final Project](https://img.shields.io/badge/Status-Final%20Project-orange?style=for-the-badge)

---

A powerful and interactive GUI tool for encrypting and decrypting text using multiple classical cryptographic algorithms, with support for applying several layers of encryption/decryption in sequence.

---

## 🚀 Features

- Multiple classical algorithms:
  - Caesar Cipher
  - Playfair Cipher
  - Vigenère Cipher
  - Columnar Transposition (Row-Column)
  - Monoalphabetic Cipher
  - Rail Fence Cipher (Zigzag)

- Multi-layer encryption/decryption.
- Material-style modern GUI with `ttkbootstrap`.
- Step-by-step result explanation.
- Supports English input only for cleaner processing.

---

## 🖼️ Interface Preview

<img src="demo.png" alt="App Screenshot" width="700"/>


---

## 🧠 How to Use

1. Enter the input text.
2. Choose the operation (`Encrypt` or `Decrypt`).
3. Select an algorithm and provide a valid key.
4. Click `➕ Add Layer` to queue the operation.
5. Add more layers as needed.
6. Click `🚀 Execute` to process all layers.
7. Output with detailed steps will appear below.

---

## 🔑 Key Rules

| Algorithm         | Key Type     |
|------------------|--------------|
| Caesar           | Numeric      |
| Zigzag (Railfence)| Numeric      |
| Row Column       | Sequence of digits (e.g., `312`) |
| Playfair         | Alphabetic   |
| Vigenère         | Alphabetic   |
| Monoalphabetic   | No key (auto-generated) |

---

## 🛠️ Requirements

- Python 3.7+
- [`ttkbootstrap`](https://ttkbootstrap.readthedocs.io/)

Install it via:

```bash
pip install ttkbootstrap
