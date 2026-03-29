# Group Name: SYDN 05 | HIT 137 Software Now | Assignment 2
##########################################################
# Group Members:
# Ashfaq Afzal Chowdhury - S399270
# Mahinur Rahman - S398451
# Tufayel Ahmed - S397780
# Ahnaf Hasnain Nahiun - S400103


##################################################################
# Question 1, Part 1, Encryption Logic. 
# Solution by Ashfaq Afzal Chowdhury - S399270
##################################################################

def build_encrypt_map(shift1, shift2):
    """
    Builds a dictionary that maps every letter to its encrypted version.

    Parameters:
        shift1 (int): First shift value entered by the user
        shift2 (int): Second shift value entered by the user

    Returns:
        encrypt_map (dict): Maps each original letter to its encrypted letter
    """
    encrypt_map = {}

    # Lowercase first half: a to m
    # Rule: shift FORWARD by shift1 * shift2
    for ch in 'abcdefghijklm':
        offset = ord(ch) - ord('a')                    # get position 0-12
        new_offset = (offset + shift1 * shift2) % 26   # shift forward, wrap at 26
        encrypt_map[ch] = chr(ord('a') + new_offset)

    # Lowercase second half: n to z
    # Rule: shift BACKWARD by shift1 + shift2
    for ch in 'nopqrstuvwxyz':
        offset = ord(ch) - ord('a')                      # get position 13-25
        new_offset = (offset - (shift1 + shift2)) % 26  # shift backward, wrap at 26
        encrypt_map[ch] = chr(ord('a') + new_offset)

    # Uppercase first half: A to M
    # Rule: shift BACKWARD by shift1
    for ch in 'ABCDEFGHIJKLM':
        offset = ord(ch) - ord('A')          # get position 0-12
        new_offset = (offset - shift1) % 26  # shift backward, wrap at 26
        encrypt_map[ch] = chr(ord('A') + new_offset)

    #  Uppercase second half: N to Z 
    # Rule: shift FORWARD by shift2 squared
    for ch in 'NOPQRSTUVWXYZ':
        offset = ord(ch) - ord('A')               # get position 13-25
        new_offset = (offset + shift2 ** 2) % 26  # shift forward by shift2^2
        encrypt_map[ch] = chr(ord('A') + new_offset)

    return encrypt_map


##################################################################
# Question 1, Part 2, Decryption Logic. 
# Solution by 
##################################################################



##################################################################
# Question 1, Part 3, File Operations.
# Solution by 
##################################################################


##################################################################
# Question 1, Part 4, Verification & Main Program Logic.
# Solution by 
##################################################################

