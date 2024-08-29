import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_symbols=True):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    symbols = string.punctuation if include_symbols else ''
    
    # Combine all selected character sets
    all_characters = lower + upper + digits + symbols
    
    # Ensure at least one character from each selected set is included
    password = [
        random.choice(lower),
        random.choice(upper) if include_uppercase else '',
        random.choice(digits) if include_digits else '',
        random.choice(symbols) if include_symbols else ''
    ]
    
    # Fill the rest of the password length with random characters from the selected set
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle to ensure the password is random
    random.shuffle(password)
    
    return ''.join(password)

# User input for password generation
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

# Generate the password
password = generate_password(length, include_uppercase, include_digits, include_symbols)
print("Generated Password:", password)
