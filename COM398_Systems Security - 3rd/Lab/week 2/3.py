from cryptography.fernet import Fernet
import base64
import time
import os
import random

class SpyMission:
    def __init__(self):
        self.agent_key = None
        self.headquarters_key = Fernet.generate_key()
        self.mission_status = "ACTIVE"
        self.locations = ["Paris", "Tokyo", "New York", "London", "Moscow"]
        self.targets = ["The Shadow", "Doctor X", "The Phantom", "Madame Y"]
        self.mission_types = ["Surveillance", "Data Recovery", "Asset Protection"]

    def display_banner(self):
        banner = """
        ╔═══════════════════════════════════════════════════╗
        ║             TOP SECRET - EYES ONLY               ║
        ║         STRATEGIC HOMELAND INTERVENTION,         ║
        ║         ENFORCEMENT & CRYPTOGRAPHY UNIT         ║
        ║                                                 ║
        ║             Operation: Dark Cipher              ║
        ║         Designed by: Agent Babashaheer          ║
        ╚═══════════════════════════════════════════════════╝
        """
        print(banner)

    def typing_effect(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()

    def generate_mission(self):
        location = random.choice(self.locations)
        target = random.choice(self.targets)
        mission_type = random.choice(self.mission_types)
        return f"Mission: {mission_type} in {location} tracking {target}"

    def encrypt_message(self, message):
        if not self.agent_key:
            self.agent_key = Fernet.generate_key()
            print("\n[SYSTEM] Your unique agent key has been generated.")
            print(f"KEY ID: {self.agent_key.decode()}")
            print("KEEP THIS KEY SECURE - YOU'LL NEED IT FOR DECRYPTION\n")
        
        f = Fernet(self.agent_key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, encrypted_message, key):
        try:
            f = Fernet(key.encode() if isinstance(key, str) else key)
            decrypted_message = f.decrypt(encrypted_message).decode()
            return decrypted_message
        except Exception as e:
            return "DECRYPTION FAILED - INVALID KEY OR MESSAGE"

    def run_mission(self):
        self.display_banner()
        self.typing_effect("\n[CONNECTING TO SECURE SERVER...]")
        time.sleep(1)
        self.typing_effect("[CONNECTION ESTABLISHED]")
        time.sleep(0.5)

        while self.mission_status == "ACTIVE":
            print("\n═══════════════════════════════════════")
            print("        AVAILABLE OPERATIONS            ")
            print("═══════════════════════════════════════")
            print("1. Send Encrypted Message to HQ")
            print("2. Decrypt Message from HQ")
            print("3. Generate New Mission Parameters")
            print("4. Abort Mission (Exit)")
            
            choice = input("\nEnter operation number: ")

            if choice == "1":
                print("\n[HQ] SECURE MESSAGE TRANSMISSION SYSTEM")
                message = input("Enter your message for HQ: ")
                encrypted = self.encrypt_message(message)
                print("\n[ENCRYPTING MESSAGE...]")
                time.sleep(1)
                print("\n[ENCRYPTED MESSAGE FOLLOWS]")
                print("─" * 50)
                print(encrypted.decode())
                print("─" * 50)

            elif choice == "2":
                print("\n[HQ] SECURE MESSAGE DECRYPTION SYSTEM")
                encrypted_msg = input("Enter encrypted message: ")
                key = input("Enter your agent key: ")
                print("\n[DECRYPTING MESSAGE...]")
                time.sleep(1)
                decrypted = self.decrypt_message(encrypted_msg.encode(), key)
                print("\n[DECRYPTED MESSAGE FOLLOWS]")
                print("─" * 50)
                print(decrypted)
                print("─" * 50)

            elif choice == "3":
                print("\n[GENERATING NEW MISSION PARAMETERS...]")
                time.sleep(1)
                new_mission = self.generate_mission()
                encrypted_mission = self.encrypt_message(new_mission)
                print("\n[NEW MISSION DETAILS - ENCRYPTED]")
                print("─" * 50)
                print(encrypted_mission.decode())
                print("─" * 50)

            elif choice == "4":
                self.typing_effect("\n[TERMINATING SECURE CONNECTION...]")
                time.sleep(1)
                self.typing_effect("[WIPING MISSION DATA...]")
                time.sleep(0.5)
                self.typing_effect("[MISSION ABORTED - STAY SAFE AGENT]")
                self.mission_status = "ABORTED"
                break

            else:
                print("\n[ERROR] Invalid operation code. Try again.")

if __name__ == "__main__":
    mission = SpyMission()
    mission.run_mission()