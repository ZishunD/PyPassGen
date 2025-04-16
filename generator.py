import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
