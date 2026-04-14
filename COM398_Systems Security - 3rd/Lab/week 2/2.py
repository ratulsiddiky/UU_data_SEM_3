from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_banner():
    banner = """
    ╔════════════════════════════════════════════════╗
    ║        Symmetric Encryption Examples           ║
    ║        Designed by: Babashaheer               ║
    ║                                               ║
    ║        Available Algorithms:                  ║
    ║        1. Caesar Cipher (Educational)         ║
    ║        2. AES-256 (Modern, Secure)           ║
    ║        3. Triple DES (Legacy)                ║
    ╚════════════════════════════════════════════════╝
    """
    print(banner)

def caesar_cipher(text, shift, mode='encrypt'):
    """Simple Caesar Cipher implementation (for educational purposes)"""
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def pad_text(text):
    """Pad text to be multiple of 16 bytes"""
    padding_length = 16 - (len(text) % 16)
    padding = bytes([padding_length] * padding_length)
    return text.encode() + padding

def unpad_text(padded_text):
    """Remove padding from decrypted text"""
    padding_length = padded_text[-1]
    return padded_text[:-padding_length]

def aes_encrypt(text, key):
    """AES-256 encryption"""
    if len(key) < 32:  # Ensure key is 32 bytes
        key = key.ljust(32, '*').encode()
    else:
        key = key[:32].encode()
    
    iv = os.urandom(16)  # Generate random IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padded_text = pad_text(text)
    ciphertext = encryptor.update(padded_text) + encryptor.finalize()
    
    # Combine IV and ciphertext and encode in base64
    return base64.b64encode(iv + ciphertext)

def aes_decrypt(encrypted_data, key):
    """AES-256 decryption"""
    if len(key) < 32:
        key = key.ljust(32, '*').encode()
    else:
        key = key[:32].encode()
    
    # Decode from base64 and separate IV and ciphertext
    encrypted_bytes = base64.b64decode(encrypted_data)
    iv = encrypted_bytes[:16]
    ciphertext = encrypted_bytes[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    padded_text = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad_text(padded_text).decode()

def triple_des_encrypt(text, key):
    """Triple DES encryption"""
    if len(key) < 24:  # Ensure key is 24 bytes
        key = key.ljust(24, '*').encode()
    else:
        key = key[:24].encode()
    
    iv = os.urandom(8)  # Triple DES uses 8-byte IV
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padded_text = pad_text(text)
    ciphertext = encryptor.update(padded_text) + encryptor.finalize()
    
    return base64.b64encode(iv + ciphertext)

def triple_des_decrypt(encrypted_data, key):
    """Triple DES decryption"""
    if len(key) < 24:
        key = key.ljust(24, '*').encode()
    else:
        key = key[:24].encode()
    
    encrypted_bytes = base64.b64decode(encrypted_data)
    iv = encrypted_bytes[:8]
    ciphertext = encrypted_bytes[8:]
    
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    padded_text = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad_text(padded_text).decode()

def main():
    generate_banner()
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            print("\n=== Encryption Mode ===")
            print("Choose encryption algorithm:")
            print("1. Caesar Cipher (Educational)")
            print("2. AES-256 (Modern, Secure)")
            print("3. Triple DES (Legacy)")
            
            algo_choice = input("Enter algorithm choice (1/2/3): ")
            message = input("Enter the message to encrypt: ")
            
            try:
                if algo_choice == "1":
                    shift = int(input("Enter shift value (1-25): "))
                    encrypted = caesar_cipher(message, shift)
                    print("\nEncryption Successful!")
                    print(f"Algorithm: Caesar Cipher (shift={shift})")
                    print("Encrypted message:", encrypted)
                
                elif algo_choice == "2":
                    key = input("Enter encryption key: ")
                    encrypted = aes_encrypt(message, key)
                    print("\nEncryption Successful!")
                    print("Algorithm: AES-256")
                    print("Encrypted message:", encrypted.decode())
                
                elif algo_choice == "3":
                    key = input("Enter encryption key: ")
                    encrypted = triple_des_decrypt(message, key)
                    print("\nEncryption Successful!")
                    print("Algorithm: Triple DES")
                    print("Encrypted message:", encrypted.decode())
                
                else:
                    print("Invalid algorithm choice!")
                    
            except Exception as e:
                print("Encryption failed:", str(e))
        
        elif choice == "2":
            print("\n=== Decryption Mode ===")
            print("Choose decryption algorithm:")
            print("1. Caesar Cipher (Educational)")
            print("2. AES-256 (Modern, Secure)")
            print("3. Triple DES (Legacy)")
            
            algo_choice = input("Enter algorithm choice (1/2/3): ")
            
            try:
                if algo_choice == "1":
                    message = input("Enter the encrypted message: ")
                    shift = int(input("Enter shift value (1-25): "))
                    decrypted = caesar_cipher(message, shift, mode='decrypt')
                    print("\nDecryption Successful!")
                    print("Decrypted message:", decrypted)
                
                elif algo_choice == "2":
                    message = input("Enter the encrypted message: ")
                    key = input("Enter decryption key: ")
                    decrypted = aes_decrypt(message.encode(), key)
                    print("\nDecryption Successful!")
                    print("Decrypted message:", decrypted)
                
                elif algo_choice == "3":
                    message = input("Enter the encrypted message: ")
                    key = input("Enter decryption key: ")
                    decrypted = triple_des_decrypt(message.encode(), key)
                    print("\nDecryption Successful!")
                    print("Decrypted message:", decrypted)
                
                else:
                    print("Invalid algorithm choice!")
                    
            except Exception as e:
                print("Decryption failed:", str(e))
                print("Make sure you have the correct message and key.")
        
        elif choice == "3":
            print("\nThank you for using the symmetric encryption examples tool!")
            break
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()