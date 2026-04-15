# PART 4 - Verification & Main Program (Contributor: Person 4)
# Verifies decryption and ties all parts together.


def verify():

    # Read the original raw file
    with open("raw_text.txt", "r") as f:
        original = f.read()

    # Read the decrypted output file
    with open("decrypted_text.txt", "r") as f:
        decrypted = f.read()

    if original == decrypted:
        print("Verification SUCCESS: Decrypted text matches the original.")
    else:
        print("Verification FAILED: Decrypted text does NOT match the original.")
        # Find and show the first character that differs
        for i, (o, d) in enumerate(zip(original, decrypted)):
            if o != d:
                print(f"  First difference at index {i}: original={repr(o)}, decrypted={repr(d)}")
                break

    return original == decrypted


# =============================================================================
# Main Entry Point
# Runs all 4 steps in order when the script is executed directly.
# =============================================================================
if __name__ == "__main__":
    # Step 1: Get shift values from user
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt(shift1, shift2)   # Step 2: encrypt raw_text.txt
    decrypt(shift1, shift2)   # Step 3: decrypt encrypted_text.txt
    verify()                  # Step 4: verify decrypted matches the original file
