import secrets
prefix = "fd" + secrets.token_hex(5)
print(":".join(prefix[i:i+4] for i in range(0, 12, 4)) + "::/48")
