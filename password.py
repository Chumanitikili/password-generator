import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    upper = input("Include uppercase? (y/n): ").lower() == "y"
    digits = input("Include digits? (y/n): ").lower() == "y"
    special = input("Include special chars? (y/n): ").lower() == "y"
    password = generate_password(length, upper, digits, special)
    print(f"Generated password: {password}")

