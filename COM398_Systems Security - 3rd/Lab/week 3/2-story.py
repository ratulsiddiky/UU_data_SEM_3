from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
import base64
import os
import time

class Person:
    def __init__(self, name):
        self.name = name
        self.private_key = None
        self.public_key = None
    
    def generate_keys(self):
        """Generate public and private key pair"""
        print(f"\n🔑 Generating keys for {self.name}...")
        time.sleep(1)  # Simulate key generation time
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        print(f"✅ Keys generated for {self.name}")

def encrypt_message(message, public_key):
    """Encrypt a message using recipient's public key"""
    try:
        encrypted = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(encrypted).decode()
    except Exception as e:
        print(f"Encryption error: {e}")
        return None

def decrypt_message(encrypted_message, private_key):
    """Decrypt a message using recipient's private key"""
    try:
        encrypted = base64.b64decode(encrypted_message.encode())
        decrypted = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()
    except Exception as e:
        print(f"Decryption error: {e}")
        return None

def sign_message(message, private_key):
    """Sign a message using sender's private key"""
    try:
        signature = private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()
    except Exception as e:
        print(f"Signing error: {e}")
        return None

def verify_signature(message, signature, public_key):
    """Verify message signature using sender's public key"""
    try:
        signature_bytes = base64.b64decode(signature.encode())
        public_key.verify(
            signature_bytes,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Verification error: {e}")
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_demo():
    try:
        clear_screen()
        print("\n=== Welcome to the Cryptographic Demo ===\n")

        # Create participants
        print("Creating participants...")
        alice = Person("Alice")
        bob = Person("Bob")

        # Generate keys
        alice.generate_keys()
        bob.generate_keys()

        # Get message
        message = input("\nEnter your secure transaction message (e.g., 'Transfer $500 to Account #12345'): ")

        # Encryption process
        print("\n=== Encrypting the Message ===\n")
        print("Alice is using Bob's public key to encrypt the message. This ensures that:")
        print("- Only Bob can read the message")
        print("- Even if intercepted, no one else can understand it")
        print("- The message remains confidential during transmission")
        
        encrypted_message = encrypt_message(message, bob.public_key)
        if encrypted_message:
            print(f"\nEncrypted message: {encrypted_message[:50]}...")
        else:
            raise Exception("Encryption failed")

        # Signing process
        print("\n=== Creating Digital Signature ===\n")
        print("Alice is now signing the message with her private key. This:")
        print("- Proves Alice really sent it")
        print("- Shows the message hasn't been tampered with")
        print("- Prevents Alice from denying she sent it later")
        
        signature = sign_message(message, alice.private_key)
        if signature:
            print(f"\nDigital signature: {signature[:50]}...")
        else:
            raise Exception("Signing failed")

        input("\nPress Enter to continue to message reception...")

        # Decryption and verification
        print("\n=== Message Reception and Verification ===\n")
        decrypted_message = decrypt_message(encrypted_message, bob.private_key)
        if decrypted_message:
            print(f"Decrypted message: {decrypted_message}")
        else:
            raise Exception("Decryption failed")

        is_valid = verify_signature(message, signature, alice.public_key)
        if is_valid:
            print("\n✅ Signature verified! The message is authentic and from Alice.")
        else:
            print("\n❌ Invalid signature! The message may have been tampered with.")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        return False

    return True

if __name__ == "__main__":
    while True:
        if run_demo():
            again = input("\nWould you like to try another message? (y/n): ")
            if again.lower() != 'y':
                break
        else:
            retry = input("\nWould you like to retry? (y/n): ")
            if retry.lower() != 'y':
                break

    print("\nThank you for using the Cryptographic Demo!")
