import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess

def open_sdes():
    subprocess.Popen(["python", "SDES.py"])

def open_final():
    subprocess.Popen(["python", "final_project.py"])
    
def open_AES():
    subprocess.Popen(["python", "AES.py"])

def placeholder(name):
    popup = ttk.Toplevel(root)
    popup.title("Coming Soon")
    ttk.Label(popup, text=f"{name} GUI is not ready yet!", font=("Helvetica", 12)).pack(pady=15, padx=15)
    ttk.Button(popup, text="OK", command=popup.destroy, bootstyle="secondary").pack(pady=10)

root = ttk.Window(themename="darkly")  #& try themes like: darkly, flatly, morph, vapor, yeti
root.title("🔐 Encryption Main Menu")
root.geometry("450x450")

ttk.Label(root, text="choose an option:", font=("Helvetica", 18, "bold")).pack(pady=30)

ttk.Button(root, text="1. SDES", command=open_sdes, width=30, bootstyle="success").pack(pady=10)
ttk.Button(root, text="2. Final Project", command=open_final, width=30, bootstyle="primary").pack(pady=10)
ttk.Button(root, text="3. AES", command=open_AES, width=30, bootstyle="warning").pack(pady=10)

ttk.Button(root, text="❌ Exit", command=root.destroy, width=30, bootstyle="danger").pack(pady=20)

root.mainloop()