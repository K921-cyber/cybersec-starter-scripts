# file_integrity.py

import hashlib

def get_file_hash(filename, algorithm='sha256'):
    """Compute hash of a file."""
    hasher = hashlib.new(algorithm)
    try:
        with open(filename, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    filename = input("Enter filename to check: ")
    expected_hash = input("Enter expected SHA-256 hash: ")
    
    actual_hash = get_file_hash(filename)
    if actual_hash is None:
        print("❌ File not found.")
    elif actual_hash == expected_hash:
        print("✅ File integrity verified!")
    else:
        print("⚠️  File has been modified!")
        print(f"Expected: {expected_hash}")

        print(f"Actual:   {actual_hash}")







