
import re

def check_password_strength(password):
    """
    Checks password strength based on:
    - Length >= 8
    - Contains uppercase, lowercase, digit, and special char
    """
    if len(password) < 8:
        return False, "Password too short (min 8 chars)"
    
    if not re.search(r"[A-Z]", password):
        return False, "Missing uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return False, "Missing lowercase letter"
    
    if not re.search(r"\d", password):
        return False, "Missing digit"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Missing special character"
    
    return True, "Password is strong!"

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    is_strong, msg = check_password_strength(pwd)
    print(msg)