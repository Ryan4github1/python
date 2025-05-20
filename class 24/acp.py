import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    all_chars = lower + upper + digits
    password_chars += random.choices(all_chars, k=length - len(password_chars))
    random.shuffle(password_chars)

    return ''.join(password_chars)
print("Generated password:", generate_password(12))