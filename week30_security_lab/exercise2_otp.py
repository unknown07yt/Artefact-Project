import hashlib
import datetime

def hash_func(data):
    return hashlib.sha256(data.encode()).hexdigest()

password = "mypassword"
salt = "abc123"

print("Registering user...")
HSP = hash_func(password + salt)
print("Stored hash:", HSP)

print("\nLogin attempt...")
time_now = str(datetime.datetime.now())
new_hsp = hash_func(HSP + time_now)
otp = new_hsp[-6:]
print("OTP sent to user:", otp)

user_input = input("Enter OTP: ")
if user_input == otp:
    print("Login accepted")
else:
    print("Login rejected")