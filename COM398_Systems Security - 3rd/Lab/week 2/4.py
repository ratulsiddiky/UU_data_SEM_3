import time
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

class VisualEncryptionLab:
    def __init__(self):
        self.box_width = 50
        
    def display_banner(self):
        banner = """
        ╔═══════════════════════════════════════════════════╗
        ║           Visual Encryption Laboratory            ║
        ║              By: Babashaheer                     ║
        ║                                                  ║
        ║     "See How Encryption Transforms Your Data"    ║
        ╚═══════════════════════════════════════════════════╝
        """
        print(banner)

    def draw_box(self, content, title=""):
        width = self.box_width
        print("\n" + "═" * width)
        if title:
            print(f"║ {title.center(width-4)} ║")
            print("═" * width)
        
        # Split content into lines that fit the box
        words = content.split()
        lines = []
        current_line = []
        
        for word in words:
            if len(" ".join(current_line + [word])) <= width-4:
                current_line.append(word)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
        if current_line:
            lines.append(" ".join(current_line))
            
        for line in lines:
            print(f"║ {line:<{width-4}} ║")
        print("═" * width)

    def show_binary_representation(self, text):
        binary = ' '.join(format(ord(char), '08b') for char in text[:10])
        self.draw_box(binary, "Binary Form (First 10 chars)")
        time.sleep(1)

    def visualize_encryption_steps(self, text, method="XOR"):
        print("\n[VISUALIZATION OF ENCRYPTION PROCESS]")
        
        # Step 1: Show original text
        self.draw_box(text, "Original Message")
        time.sleep(1)
        
        # Step 2: Show binary
        self.show_binary_representation(text)
        
        # Step 3: Show encryption method
        if method == "XOR":
            key = os.urandom(len(text))
            self.draw_box("Applying XOR operation with key...", "Encryption Step")
            encrypted = bytes(a ^ b for a, b in zip(text.encode(), key))
        else:
            key = os.urandom(32)
            self.draw_box("Applying AES encryption...", "Encryption Step")
            cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
            encryptor = cipher.encryptor()
            # Pad the text
            padded = text.encode() + b'\0' * (16 - len(text) % 16)
            encrypted = encryptor.update(padded) + encryptor.finalize()
        
        time.sleep(1)
        
        # Step 4: Show encrypted result
        encrypted_b64 = base64.b64encode(encrypted).decode()
        self.draw_box(encrypted_b64[:40] + "...", "Encrypted Result")
        
        return encrypted, key

    def demonstrate_encryption_properties(self):
        print("\n[DEMONSTRATING ENCRYPTION PROPERTIES]")
        
        # Property 1: Same input, different keys
        message = "Hello World!"
        self.draw_box("Property 1: Same input, different keys produce different outputs", "DEMONSTRATION")
        time.sleep(1)
        
        for i in range(2):
            encrypted, _ = self.visualize_encryption_steps(message)
            time.sleep(1)
        
        # Property 2: Small change in input
        self.draw_box("Property 2: Small change in input causes large change in output", "DEMONSTRATION")
        message1 = "Hello World!"
        message2 = "Hello World."
        
        enc1, key = self.visualize_encryption_steps(message1)
        time.sleep(1)
        enc2, _ = self.visualize_encryption_steps(message2)
        time.sleep(1)

    def interactive_lab(self):
        self.display_banner()
        
        while True:
            print("\nChoose an experiment:")
            print("1. Visualize Encryption Process")
            print("2. Demonstrate Encryption Properties")
            print("3. Interactive Message Encryption")
            print("4. Exit Laboratory")
            
            choice = input("\nSelect experiment number: ")
            
            if choice == "1":
                message = input("\nEnter a message to encrypt: ")
                self.visualize_encryption_steps(message)
                
            elif choice == "2":
                self.demonstrate_encryption_properties()
                
            elif choice == "3":
                print("\n[INTERACTIVE ENCRYPTION EXPERIMENT]")
                message = input("Enter first message: ")
                key = os.urandom(32)
                
                # First encryption
                encrypted1, _ = self.visualize_encryption_steps(message, "AES")
                
                # Show how same key produces same output
                print("\nUsing same key for same input:")
                encrypted2, _ = self.visualize_encryption_steps(message, "AES")
                
                # Show how different input produces different output
                print("\nUsing same key for different input:")
                new_message = input("Enter a slightly different message: ")
                encrypted3, _ = self.visualize_encryption_steps(new_message, "AES")
                
            elif choice == "4":
                print("\nThank you for using the Visual Encryption Laboratory!")
                print("Remember: Understanding encryption is key to cybersecurity!")
                break
                
            else:
                print("Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    lab = VisualEncryptionLab()
    lab.interactive_lab()