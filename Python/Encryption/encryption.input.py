def encrypt():
    text = input("What is the text? ")
    shift = int(input("How many numbers? "))
    
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine the ASCII offset (65 for uppercase, 97 for lowercase)
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character and wrap around the alphabet
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char
    
    print(f"The encrypted text is: {encrypted_text}")

# Call the function
encrypt()