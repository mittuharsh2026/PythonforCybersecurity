import random, string, hashlib, requests

chars = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(random.choice(chars) for i in range(16))

sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
prefix, suffix = sha1[:5], sha1[5:]

url = f"https://api.pwnedpasswords.com/range/{prefix}"
response = requests.get(url)

if suffix in response.text:
    print("Password was found in a data breach. Try again.")
else:
    print("Secure password:", password)
