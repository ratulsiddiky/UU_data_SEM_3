from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
import base64
import os
import time
import sys

def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🔐 Asymmetric Cryptography Interactive Learning 🔐      ║
║                 Designed by Babashaheer                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_transfer(length=40):
    for i in range(length):
        sys.stdout.write('\r')
        sys.stdout.write('=' * i + '>' + ' ' * (length - i))
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Person:
    def __init__(self, name):
        self.name = name
        self.private_key = None
        self.public_key = None
    
    def generate_keys(self):
        animate_text(f"🔑 Generating secure keys for {self.name}...")
        time.sleep(1)
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        animate_text(f"✅ Keys generated successfully for {self.name}!")

def encrypt_message(message, public_key):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(encrypted).decode()

def sign_message(message, private_key):
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

def decrypt_message(encrypted_message, private_key):
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

def run_demo():
    while True:
        clear_screen()
        print_banner()
        
        # Step 1: Get participant names
        animate_text("\n📝 Step 1: Let's meet our participants!")
        sender_name = input("\nEnter sender's name: ")
        receiver_name = input("Enter receiver's name: ")
        
        # Step 2: Generate keys
        animate_text("\n🔐 Step 2: Generating secure keys...")
        sender = Person(sender_name)
        receiver = Person(receiver_name)
        
        input("\nPress Enter to generate keys...")
        sender.generate_keys()
        receiver.generate_keys()
        
        # Step 3: Write message
        animate_text(f"\n✍️  Step 3: {sender_name} will write a message")
        message = input(f"\nEnter your message, {sender_name}: ")
        
        ready = input("\nAre you ready to encrypt and hash the message? (y/n): ")
        if ready.lower() != 'y':
            continue
            
        # Step 4: Show encryption process
        animate_text("\n🔒 Step 4: Encrypting and hashing the message")
        animate_text("\nCalculating message hash...")
        time.sleep(1)
        animate_text("Preparing encryption...")
        time.sleep(1)
        
        # Step 5: Sign with sender's private key
        animate_text(f"\n✍️  Step 5: {sender_name} is signing the message with their private key")
        signature = sign_message(message, sender.private_key)
        animate_text("Signature created!")
        
        # Step 6: Encrypt with receiver's public key
        animate_text(f"\n🔐 Step 6: Encrypting message with {receiver_name}'s public key")
        encrypted_message = encrypt_message(message, receiver.public_key)
        animate_text("Message encrypted!")
        
        # Step 7: Show message transfer
        animate_text(f"\n📨 Step 7: Sending encrypted message to {receiver_name}")
        animate_transfer()
        
        # Step 8: Receiver confirmation
        input(f"\n{receiver_name}, press Enter to receive the message...")
        
# Step 9: Decrypt message
        animate_text(f"\n🔓 Step 9: Decryption Process for {receiver_name}")
        animate_text("\nTo decrypt the message, we need to use your private key.")
        input("\nPress Enter to start decryption process...")
        
        animate_text("\nDecryption steps:")
        animate_text("1. Converting encrypted message from base64...")
        time.sleep(1)
        animate_text("2. Applying your private key...")
        time.sleep(1)
        animate_text("3. Removing padding...")
        time.sleep(1)
        
        decrypted_message = decrypt_message(encrypted_message, receiver.private_key)
        animate_text("\n✅ Message successfully decrypted!")
        print(f"\nDecrypted message: {decrypted_message}")
        
        input("\nPress Enter to proceed to message verification...")
        
        # Step 10: Verify integrity
        animate_text(f"\n🔍 Step 10: Message Integrity Verification")
        animate_text(f"\nNow we need to verify if this message really came from {sender_name}")
        animate_text(f"and hasn't been tampered with during transmission.")
        
        input("\nPress Enter to start verification process...")
        
        animate_text("\nVerification steps:")
        animate_text(f"1. Using {sender_name}'s public key...")
        time.sleep(1)
        animate_text("2. Verifying digital signature...")
        time.sleep(1)
        animate_text("3. Checking message integrity...")
        time.sleep(1)
        
        is_valid = verify_signature(message, signature, sender.public_key)
        
        # Step 11: Show detailed results
        animate_text("\n📝 Step 11: Verification Results")
        
        if is_valid:
            animate_text("\n✅ Message Verification Results:")
            animate_text(f"1. Signature is valid - confirmed from {sender_name}")
            animate_text("2. Message integrity check passed")
            animate_text("3. No tampering detected")
            animate_text(f"\nFinal verified message: {decrypted_message}")
            input("\nPress Enter to continue...")
        else:
            animate_text("\n❌ Warning! Security Check Failed:")
            animate_text("1. Signature verification failed")
            animate_text("2. Message might have been tampered with")
            animate_text("3. Cannot confirm sender's identity")
            input("\nPress Enter to continue...")
        
        # Step 12: Understanding confirmation
        understand = input("\nDo you understand how this works? (yes/no): ")
        
        # Step 13 & 14: Handle response
        if understand.lower() == 'no':
            animate_text("\nLet's go through it again!")
            input("Press Enter to restart...")
            continue
        else:
            animate_text("\n🎉 Congratulations! You've learned about asymmetric cryptography!")
            animate_text("Key points to remember:")
            animate_text("1. Public keys are for encryption and verification")
            animate_text("2. Private keys are for decryption and signing")
            animate_text("3. Always keep private keys secret!")
            
            again = input("\nWould you like to try another example? (y/n): ")
            if again.lower() != 'y':
                break

    animate_text("\nThank you for learning about cryptography! Stay secure! 🔐")

if __name__ == "__main__":
    run_demo()
