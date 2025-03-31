from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
    """
    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        return True
    return False

# Example Usage
stored_logins = {
    "qamar@example.com": hash_password("password123"),
    "zafar@example.com": hash_password("mysecurepass")
}

email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, stored_logins, password):
    print("Login Successful ✅")
else:
    print("Login Failed ❌ (Wrong Email or Password)")
