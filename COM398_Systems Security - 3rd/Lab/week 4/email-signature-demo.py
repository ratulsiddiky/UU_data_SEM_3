import hashlib
import os
from datetime import datetime

class EmailSystem:
    def __init__(self):
        self.private_key = "123456789abcdef"
        self.public_key = "abcdef123456789"
    
    def sign_email(self, sender, recipient, subject, content):
        email_content = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\nDate: {datetime.now()}\n\n{content}"
        content_hash = hashlib.sha256(email_content.encode()).hexdigest()
        signature = hashlib.sha256((content_hash + self.private_key).encode()).hexdigest()
        return {
            'email_content': email_content,
            'signature': signature,
            'hash': content_hash
        }
    
    def verify_email(self, email_content, provided_signature):
        received_hash = hashlib.sha256(email_content.encode()).hexdigest()
        expected_signature = hashlib.sha256((received_hash + self.private_key).encode()).hexdigest()
        return provided_signature == expected_signature

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def display_header():
    print("=== Digital Signature Interactive Demo ===")
    print("Author: Baba Shaheer")
    print("----------------------------------------")

def wait_for_user():
    input("\nPress Enter to continue...")

def interactive_demo():
    email_system = EmailSystem()
    
    # Initial Welcome Screen
    clear_screen()
    display_header()
    print("\nWelcome to Digital Signature Demonstration")
    print("\nThis interactive demo will show you how digital")
    print("signatures protect email authenticity and integrity.")
    wait_for_user()
    
    # Step 1: Original Email Creation
    clear_screen()
    display_header()
    print("\nStep 1: Professor Composing Email")
    print("--------------------------------")
    print("Professor Jones needs to send a grade change request")
    print("to the registrar's office for a student.")
    wait_for_user()
    
    original_sender = "professor.jones@university.edu"
    recipient = "registrar@university.edu"
    subject = "Grade Change Request - Student ID: 12345"
    content = "Please update the grade for Student ID 12345 from B to A- based on the revised project submission."
    
    print("\nEmail Details:")
    print(f"From: {original_sender}")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Content: {content}")
    wait_for_user()
    
    # Step 2: Signing Process
    clear_screen()
    display_header()
    print("\nStep 2: Digital Signing Process")
    print("-----------------------------")
    print("1. First, the email system creates a hash of the entire message")
    print("2. Then, it encrypts this hash with the professor's private key")
    wait_for_user()
    
    signed_email = email_system.sign_email(original_sender, recipient, subject, content)
    print("\nGenerated Hash:")
    print(signed_email['hash'][:30] + "...")
    wait_for_user()
    
    print("\nDigital Signature Created:")
    print(signed_email['signature'][:30] + "...")
    wait_for_user()
    
    # Step 3: Verification of Original
    clear_screen()
    display_header()
    print("\nStep 3: Registrar's Office Receives Email")
    print("-------------------------------------")
    print("The registrar's office will now verify the email's authenticity")
    wait_for_user()
    
    is_valid = email_system.verify_email(signed_email['email_content'], signed_email['signature'])
    print("\nVerification Process:")
    print("1. Recalculate hash of received email")
    print("2. Verify signature using professor's public key")
    print(f"\nSignature Verification Result: {'VALID' if is_valid else 'INVALID'}")
    wait_for_user()
    
    # Step 4: Tampering Attempt
    clear_screen()
    display_header()
    print("\nStep 4: Simulating a Tampering Attempt")
    print("-----------------------------------")
    print("Now, let's simulate a student attempting to")
    print("intercept and modify the email...")
    wait_for_user()
    
    print("\nOriginal grade change: B to A-")
    print("Attempting to modify to: B to A+")
    tampered_content = signed_email['email_content'].replace("B to A-", "B to A+")
    wait_for_user()
    
    is_valid_tampered = email_system.verify_email(tampered_content, signed_email['signature'])
    print("\nVerifying tampered email with original signature...")
    print(f"Verification Result: {'VALID' if is_valid_tampered else 'INVALID'}")
    print("\nThe tampering was detected!")
    wait_for_user()
    
    # Step 5: Interactive Part
    while True:
        clear_screen()
        display_header()
        print("\n=== Now It's Your Turn! ===")
        print("\nWhat would you like to try?")
        print("1. Create and sign your own email")
        print("2. Try to tamper with an email")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            clear_screen()
            display_header()
            print("\n=== Create Your Own Signed Email ===")
            sender = input("Enter sender email: ")
            recipient = input("Enter recipient email: ")
            subject = input("Enter subject: ")
            content = input("Enter content: ")
            
            signed_email = email_system.sign_email(sender, recipient, subject, content)
            print("\nYour Signed Email:")
            print("------------------")
            print(signed_email['email_content'])
            print(f"\nSignature: {signed_email['signature']}")
            wait_for_user()
            
        elif choice == "2":
            clear_screen()
            display_header()
            print("\n=== Email Tampering Simulation ===")
            print("\nOriginal Email:")
            original_content = "Approving budget of $10,000 for department supplies."
            signed_email = email_system.sign_email("dean@university.edu", 
                                                 "staff@university.edu",
                                                 "Budget Approval",
                                                 original_content)
            print(signed_email['email_content'])
            print(f"\nOriginal Signature: {signed_email['signature'][:30]}...")
            
            print("\nNow, try to modify the email content.")
            print("(For example, change the amount or other details)")
            tampered_content = input("\nEnter modified content: ")
            
            is_valid = email_system.verify_email(tampered_content, signed_email['signature'])
            print(f"\nSignature verification after tampering: {'VALID' if is_valid else 'INVALID'}")
            wait_for_user()
            
        elif choice == "3":
            clear_screen()
            display_header()
            print("\nThank you for using the Digital Signature Demo!")
            break

if __name__ == "__main__":
    interactive_demo()