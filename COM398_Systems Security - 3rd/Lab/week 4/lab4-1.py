import hashlib
import os

class CryptoDemo:
    def generate_hash(self, message):
        """Generate SHA-256 hash of a message"""
        return hashlib.sha256(message.encode()).hexdigest()
    
    def generate_md5(self, message):
        """Generate MD5 hash of a message (for demonstration only - MD5 is not secure!)"""
        return hashlib.md5(message.encode()).hexdigest()

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_separator():
    print("\n" + "=" * 50 + "\n")

def interactive_demo():
    demo = CryptoDemo()
    
    while True:
        clear_screen()
        print("=== Cryptographic Hash Function Demo ===")
        print("\n1. SHA-256 Hash Demo")
        print("2. Compare Different Messages")
        print("3. Avalanche Effect Demo")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            clear_screen()
            print("=== SHA-256 Hash Demonstration ===")
            print("\nA hash function is like a digital fingerprint.")
            
            message = input("\nEnter a message to hash: ")
            hash1 = demo.generate_hash(message)
            print("\nOriginal message:", message)
            print("SHA-256 hash:", hash1)
            
            modified = input("\nNow modify the message slightly: ")
            hash2 = demo.generate_hash(modified)
            print("\nModified message:", modified)
            print("New hash:", hash2)
            
            print("\nAre the hashes same?", "Yes" if hash1 == hash2 else "No")
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            clear_screen()
            print("=== Compare Different Messages ===")
            
            print("\nLet's hash two different messages and compare them")
            msg1 = input("Enter first message: ")
            msg2 = input("Enter second message: ")
            
            hash1 = demo.generate_hash(msg1)
            hash2 = demo.generate_hash(msg2)
            
            print("\nFirst message:", msg1)
            print("Hash:", hash1)
            print("\nSecond message:", msg2)
            print("Hash:", hash2)
            
            print("\nHashes are", 'same' if hash1 == hash2 else 'different')
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            clear_screen()
            print("=== Avalanche Effect Demonstration ===")
            
            message = input("\nEnter a message: ")
            original_hash = demo.generate_hash(message)
            
            print("\nOriginal message:", message)
            print("Original hash:", original_hash)
            
            # Change one character
            modified = message[:-1] + ('1' if message[-1] != '1' else '2')
            modified_hash = demo.generate_hash(modified)
            
            print("\nModified message (changed last character):", modified)
            print("Modified hash:", modified_hash)
            
            # Show difference
            print("\nEven changing one character completely changes the hash!")
            print("Number of different characters in hash:", sum(1 for a, b in zip(original_hash, modified_hash) if a != b))
            input("\nPress Enter to continue...")
            
        elif choice == '4':
            print("\nThank you for using the demo!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    interactive_demo()
