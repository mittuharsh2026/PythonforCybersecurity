import crypt
import urllib.request
import os


GITHUB_RAW_WORDLIST_URL = "PASTE_RAW_GITHUB_LINK_HERE"

SHADOW_FILE = "shadow"
WORDLIST_FILE = "passwords.txt"
MIN_FOUND = 10


if not os.path.exists(WORDLIST_FILE):
    print("Downloading password list...")
    urllib.request.urlretrieve(GITHUB_RAW_WORDLIST_URL, WORDLIST_FILE)
    print("Download complete.")


hashes = {}

with open(SHADOW_FILE, "r", errors="ignore") as file:
    for line in file:
        parts = line.strip().split(":")
        if len(parts) >= 2:
            username = parts[0]
            password_hash = parts[1]

            if password_hash not in ["*", "!", "", "x"]:
                hashes[username] = password_hash

print(f"Loaded {len(hashes)} password hashes.")

found = {}


with open(WORDLIST_FILE, "r", errors="ignore") as file:
    for password in file:
        password = password.strip()

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
