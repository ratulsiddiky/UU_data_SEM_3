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
        
    def get_public_key_pem(self):
        """Get public key in PEM format"""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

def encrypt_message(message, public_key):
    """Encrypt a message using recipient's public key"""
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted_message, private_key):
    """Decrypt a message using recipient's private key"""
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

def sign_message(message, private_key):
    """Sign a message using sender's private key"""
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode()

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
    except:
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_step(step_num, description):
    print(f"\n📍 Step {step_num}: {description}")
    print("-" * 50)

def interactive_demo():
    while True:
        clear_screen()
        print("🔐 Asymmetric Cryptography Interactive Demo 🔐")
        print("=" * 50)
        
        # Step 1: Create participants
        print_step(1, "Creating participants (Alice and Bob)")
        alice = Person("Alice")
        bob = Person("Bob")
        input("\nPress Enter to continue...")

        # Step 2: Generate keys
        print_step(2, "Generating key pairs")
        alice.generate_keys()
        bob.generate_keys()
        input("\nPress Enter to continue...")

        # Step 3: Get message from user
        print_step(3, "Message input")
        message = input("\nEnter a message for Alice to send to Bob: ")

        # Step 4: Encrypt message
        print_step(4, "Encrypting message")
        print("\n📤 Alice is encrypting the message using Bob's public key...")
        time.sleep(1)
        encrypted_message = encrypt_message(message, bob.public_key)
        print(f"\nEncrypted message: {encrypted_message[:50]}...")
        
        # Step 5: Sign message
        print("\n✍️  Alice is signing the message with her private key...")
        time.sleep(1)
        signature = sign_message(message, alice.private_key)
        print(f"\nSignature: {signature[:50]}...")
        input("\nPress Enter to continue...")

        # Step 6: Decrypt message
        print_step(5, "Decrypting message")
        print("\n📥 Bob is decrypting the message using his private key...")
        time.sleep(1)
        decrypted_message = decrypt_message(encrypted_message, bob.private_key)
        print(f"\nDecrypted message: {decrypted_message}")

        # Step 7: Verify signature
        print_step(6, "Verifying signature")
        print("\n🔍 Bob is verifying Alice's signature using her public key...")
        time.sleep(1)
        is_valid = verify_signature(message, signature, alice.public_key)
        if is_valid:
            print("\n✅ Signature verified! Message is authentic and from Alice.")
        else:
            print("\n❌ Invalid signature! Message may have been tampered with.")

        # Ask to run again
        again = input("\nWould you like to try again? (y/n): ")
        if again.lower() != 'y':
            break

    print("\nThank you for using the Asymmetric Cryptography Demo!")

if __name__ == "__main__":
    interactive_demo()
