from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def generate_banner():
    banner = """
    ╔═══════════════════════════════════════════╗
    ║     Cryptographic Encryption Tool         ║
    ║     Designed by: Babashaheer             ║
    ║     Version: 1.0                         ║
    ║     Using: Fernet (AES-128-CBC)         ║
    ╚═══════════════════════════════════════════╝
    """
    print(banner)

def generate_key_from_password(password):
    # Convert password to bytes
    password = password.encode()
    salt = b'salt_'  # In production, use a random salt and store it
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_message(message, password):
    # Generate key from password
    key = generate_key_from_password(password)
    
    # Create cipher suite
    cipher_suite = Fernet(key)
    
    # Convert message to bytes and encrypt
    encrypted_data = cipher_suite.encrypt(message.encode())
    return encrypted_data

def decrypt_message(encrypted_message, password):
    # Generate key from password
    key = generate_key_from_password(password)
    
    # Create cipher suite
    cipher_suite = Fernet(key)
    
    # Decrypt
    decrypted_data = cipher_suite.decrypt(encrypted_message)
    return decrypted_data.decode()

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
            message = input("Enter the message to encrypt: ")
            password = input("Enter a password (this will be your secret key): ")
            
            try:
                encrypted_data = encrypt_message(message, password)
                print("\nEncryption Successful!")
                print("Encrypted message:", encrypted_data.decode())
                print("\nKeep this encrypted message and password safe for decryption.")
                
            except Exception as e:
                print("Encryption failed:", str(e))
        
        elif choice == "2":
            print("\n=== Decryption Mode ===")
            try:
                encrypted_message = input("Enter the encrypted message: ").encode()
                password = input("Enter the secret key (password): ")
                
                decrypted_data = decrypt_message(encrypted_message, password)
                print("\nDecryption Successful!")
                print("Decrypted message:", decrypted_data)
                
            except Exception as e:
                print("Decryption failed. Make sure you have the correct message and password.")
                print("Error:", str(e))
        
        elif choice == "3":
            print("\nThank you for using the encryption tool!")
            break
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
