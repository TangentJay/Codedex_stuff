import hashlib
from tkinter import *
from tkinter import messagebox

class CryptoToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Crypto Toolkit - Lab 3 Prep")
        self.root.geometry("600x500")
        self.root.configure(bg='#2b2b2b')
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        Label(self.root, text="🔐 Cryptographic Toolkit", 
              font=("Arial", 16, "bold"), fg='#00ff88', bg='#2b2b2b').pack(pady=10)
        
        # Create notebook-style tabs
        self.create_caesar_tab()
        self.create_xor_tab()
        self.create_hash_tab()
    
    def create_caesar_tab(self):
        # Caesar Cipher Section
        caesar_frame = LabelFrame(self.root, text="🏛️ Caesar Cipher", 
                                 fg='#00ffff', bg='#2b2b2b', font=("Arial", 12, "bold"))
        caesar_frame.pack(pady=10, padx=20, fill='x')
        
        Label(caesar_frame, text="Text:", fg='white', bg='#2b2b2b').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.caesar_text = Entry(caesar_frame, width=40, font=("Arial", 10))
        self.caesar_text.grid(row=0, column=1, padx=5, pady=5)
        
        Label(caesar_frame, text="Shift:", fg='white', bg='#2b2b2b').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.caesar_shift = Entry(caesar_frame, width=10, font=("Arial", 10))
        self.caesar_shift.insert(0, "3")
        self.caesar_shift.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        
        Button(caesar_frame, text="🔒 Encrypt", command=self.caesar_encrypt, 
               bg='#ff6b6b', fg='white').grid(row=2, column=0, padx=5, pady=5)
        Button(caesar_frame, text="🔓 Decrypt", command=self.caesar_decrypt, 
               bg='#51cf66', fg='white').grid(row=2, column=1, sticky='w', padx=5, pady=5)
        
        Label(caesar_frame, text="Result:", fg='white', bg='#2b2b2b').grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.caesar_result = Entry(caesar_frame, width=40, font=("Arial", 10), state='readonly')
        self.caesar_result.grid(row=3, column=1, padx=5, pady=5)
    
    def create_xor_tab(self):
        # XOR Cipher Section
        xor_frame = LabelFrame(self.root, text="⚡ XOR Cipher", 
                              fg='#00ffff', bg='#2b2b2b', font=("Arial", 12, "bold"))
        xor_frame.pack(pady=10, padx=20, fill='x')
        
        Label(xor_frame, text="Text:", fg='white', bg='#2b2b2b').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.xor_text = Entry(xor_frame, width=40, font=("Arial", 10))
        self.xor_text.grid(row=0, column=1, padx=5, pady=5)
        
        Label(xor_frame, text="Key:", fg='white', bg='#2b2b2b').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.xor_key = Entry(xor_frame, width=40, font=("Arial", 10))
        self.xor_key.insert(0, "secret")
        self.xor_key.grid(row=1, column=1, padx=5, pady=5)
        
        Button(xor_frame, text="🔄 XOR Encrypt/Decrypt", command=self.xor_cipher, 
               bg='#339af0', fg='white').grid(row=2, column=0, columnspan=2, pady=5)
        
        Label(xor_frame, text="Result:", fg='white', bg='#2b2b2b').grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.xor_result = Entry(xor_frame, width=40, font=("Arial", 10), state='readonly')
        self.xor_result.grid(row=3, column=1, padx=5, pady=5)
    
    def create_hash_tab(self):
        # Hash Generator Section
        hash_frame = LabelFrame(self.root, text="🔢 Hash Generator", 
                               fg='#00ffff', bg='#2b2b2b', font=("Arial", 12, "bold"))
        hash_frame.pack(pady=10, padx=20, fill='x')
        
        Label(hash_frame, text="Text:", fg='white', bg='#2b2b2b').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.hash_text = Entry(hash_frame, width=40, font=("Arial", 10))
        self.hash_text.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
        
        Button(hash_frame, text="MD5", command=lambda: self.generate_hash('md5'), 
               bg='#fd7e14', fg='white', width=8).grid(row=1, column=0, padx=5, pady=5)
        Button(hash_frame, text="SHA-1", command=lambda: self.generate_hash('sha1'), 
               bg='#e64980', fg='white', width=8).grid(row=1, column=1, padx=5, pady=5)
        Button(hash_frame, text="SHA-256", command=lambda: self.generate_hash('sha256'), 
               bg='#7950f2', fg='white', width=8).grid(row=1, column=2, padx=5, pady=5)
        
        Label(hash_frame, text="Hash:", fg='white', bg='#2b2b2b').grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.hash_result = Text(hash_frame, width=50, height=3, font=("Consolas", 9))
        self.hash_result.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
        
        Button(hash_frame, text="📋 Copy Hash", command=self.copy_hash, 
               bg='#20c997', fg='white').grid(row=3, column=1, pady=5)
    
    def caesar_encrypt(self):
        try:
            text = self.caesar_text.get()
            shift = int(self.caesar_shift.get())
            result = self.caesar_cipher(text, shift)
            
            self.caesar_result.config(state='normal')
            self.caesar_result.delete(0, END)
            self.caesar_result.insert(0, result)
            self.caesar_result.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid shift number!")
    
    def caesar_decrypt(self):
        try:
            text = self.caesar_text.get()
            shift = -int(self.caesar_shift.get())  # Negative shift for decrypt
            result = self.caesar_cipher(text, shift)
            
            self.caesar_result.config(state='normal')
            self.caesar_result.delete(0, END)
            self.caesar_result.insert(0, result)
            self.caesar_result.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid shift number!")
    
    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                # Handle uppercase and lowercase
                start = 65 if char.isupper() else 97
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += char
        return result
    
    def xor_cipher(self):
        text = self.xor_text.get()
        key = self.xor_key.get()
        
        if not key:
            messagebox.showerror("Error", "Please enter a key!")
            return
        
        result = ""
        key_len = len(key)
        
        for i, char in enumerate(text):
            key_char = key[i % key_len]
            result += chr(ord(char) ^ ord(key_char))
        
        # Convert to hex for display (since XOR can produce unprintable chars)
        hex_result = result.encode('latin-1').hex()
        
        self.xor_result.config(state='normal')
        self.xor_result.delete(0, END)
        self.xor_result.insert(0, f"Hex: {hex_result}")
        self.xor_result.config(state='readonly')
    
    def generate_hash(self, hash_type):
        text = self.hash_text.get()
        if not text:
            messagebox.showerror("Error", "Please enter text to hash!")
            return
        
        # Generate hash
        if hash_type == 'md5':
            hash_obj = hashlib.md5(text.encode())
        elif hash_type == 'sha1':
            hash_obj = hashlib.sha1(text.encode())
        elif hash_type == 'sha256':
            hash_obj = hashlib.sha256(text.encode())
        
        hash_result = hash_obj.hexdigest()
        
        # Display result
        self.hash_result.delete(1.0, END)
        self.hash_result.insert(END, f"{hash_type.upper()}: {hash_result}")
    
    def copy_hash(self):
        hash_text = self.hash_result.get(1.0, END).strip()
        if hash_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(hash_text)
            messagebox.showinfo("Success", "Hash copied to clipboard!")

# Run the application
if __name__ == "__main__":
    root = Tk()
    app = CryptoToolkit(root)
    root.mainloop()