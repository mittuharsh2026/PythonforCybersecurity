import crypt
import os

MIN_FOUND = 10

# Change these only if your files have different names
SHADOW_FILE = "shadow"
WORDLIST_FILE = "10-million-password-list-top-1000000.txt"

# If the exact wordlist name is different, this tries to find a text wordlist
if not os.path.exists(WORDLIST_FILE):
    possible_lists = [
        "passwords.txt",
        "10-million-password-list-top-100000.txt",
        "10-million-password-list-top-1000000.txt",
        "10-million-password-list-top-10000000.txt",
        "rockyou.txt"
    ]

    for name in possible_lists:
        if os.path.exists(name):
            WORDLIST_FILE = name
            break

# Check required files
if not os.path.exists(SHADOW_FILE):
    print("ERROR: shadow file not found.")
    print("Make sure the shadow file is in the same folder as this script.")
    exit()

if not os.path.exists(WORDLIST_FILE):
    print("ERROR: password list not found.")
    print("Put your password list in the same folder as this script.")
    print("Then update WORDLIST_FILE with the exact file name.")
    exit()

# Read usernames and hashes from shadow file
hashes = {}

with open(SHADOW_FILE, "r", errors="ignore") as file:
    for line in file:
        parts = line.strip().split(":")
        if len(parts) >= 2:
            username = parts[0]
            password_hash = parts[1]

            if password_hash not in ["*", "!", "", "x"]:
                hashes[username] = password_hash

print(f"Loaded {len(hashes)} hashes.")
print(f"Using password list: {WORDLIST_FILE}")

found = {}

# Try each password against each hash
with open(WORDLIST_FILE, "r", errors="ignore") as file:
    for password in file:
        password = password.strip()

        if password == "":
            continue

        for username, password_hash in hashes.items():
            if username in found:
                continue

            test_hash = crypt.crypt(password, password_hash)

            if test_hash == password_hash:
                found[username] = password
                print(f"[FOUND] {username}: {password}")

        if len(found) >= MIN_FOUND:
            break

print("\nFinal Answers:")
for username, password in found.items():
    print(f"{username}: {password}")

print(f"\nTotal found: {len(found)}")
