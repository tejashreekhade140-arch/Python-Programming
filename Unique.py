
import time
import random

def slow_print(text, delay=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

print("=" * 45)
slow_print("      INITIALIZING PYTHON SYSTEM...", 0.03)
print("=" * 45)

time.sleep(0.5)

messages = [
    "[+] Loading Python modules...",
    "[+] Establishing secure connection...",
    "[+] Analyzing system data...",
    "[+] Running developer mode...",
    "[+] System ready!"
]

for message in messages:
    slow_print(message, 0.02)
    time.sleep(random.uniform(0.3, 0.8))

print("=" * 45)
slow_print("   ACCESS GRANTED - WELCOME DEVELOPER!", 0.03)
print("=" * 45)
