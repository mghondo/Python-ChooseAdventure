import random
import string

def generate_password():
    while True:
        try:
            length = int(input("How long do you want your password to be? "))
            symbols = int(input("How many symbols/characters do you want? "))
            numbers = int(input("How many numbers do you want? "))
            caps = int(input("How many capital letters do you want? "))

            if length < symbols + numbers + caps:
                print("Error: The sum of symbols, numbers, and capital letters exceeds the total length.")
                continue

            lowercase = length - (symbols + numbers + caps)

            if lowercase < 0:
                print("Error: There's not enough space for lowercase letters. Please adjust your inputs.")
                continue

            password = []

            # Add symbols
            password.extend(random.choices(string.punctuation, k=symbols))

            # Add numbers
            password.extend(random.choices(string.digits, k=numbers))

            # Add capital letters
            password.extend(random.choices(string.ascii_uppercase, k=caps))

            # Add lowercase letters
            password.extend(random.choices(string.ascii_lowercase, k=lowercase))

            # Shuffle the password
            random.shuffle(password)

            return ''.join(password)

        except ValueError:
            print("Please enter valid numbers for all inputs.")

# Generate and print the password
generated_password = generate_password()
print(f"Your generated password is: {generated_password}")