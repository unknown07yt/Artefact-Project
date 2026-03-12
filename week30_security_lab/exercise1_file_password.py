import hashlib

stored_hash = None

def register(file_path):
    global stored_hash
    with open(file_path, "rb") as f:
        data = f.read()
    stored_hash = hashlib.sha256(data).hexdigest()
    print("User registered successfully")

def login(file_path):
    global stored_hash
    with open(file_path, "rb") as f:
        data = f.read()
    login_hash = hashlib.sha256(data).hexdigest()
    if login_hash == stored_hash:
        print("Login successful")
    else:
        print("Login rejected")

print("Registering user...")
register("password_file.txt")

print("\nTrying correct login...")
login("password_file.txt")

print("\nTrying wrong login...")
login("wrong_file.txt")