
# PART 3 - File Operations (Contributor: Person 3)
# Handles reading, encrypting, and writing files.


def encrypt(shift1, shift2):
   
    encrypt_map = build_encrypt_map(shift1, shift2)

    # Read original text from file
    with open("raw_text.txt", "r") as f:
        raw = f.read()

    # Encrypt each character; non-letters are returned unchanged
    encrypted = ''.join(encrypt_map.get(ch, ch) for ch in raw)

    # Write encrypted content to new file
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)

    print("Encryption complete. Output written to 'encrypted_text.txt'.")


def decrypt(shift1, shift2):
   
    decrypt_map = build_decrypt_map(shift1, shift2)

    # Read encrypted text from file
    with open("encrypted_text.txt", "r") as f:
        encrypted = f.read()

    # Decrypt each character; non-letters are returned unchanged
    decrypted = ''.join(decrypt_map.get(ch, ch) for ch in encrypted)

    # Write decrypted content to new file
    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted)

    print("Decryption complete. Output written to 'decrypted_text.txt'.")
