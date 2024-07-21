import re

def validate_username(username):
    if not username:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed 50 characters."
    return "Valid username."

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special symbol."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase character."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase character."
    return "Valid password."

def validate_email(email):
    if "@" not in email:
        return "Email must contain the '@' symbol."
    if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
        return "Invalid email format."
    return "Valid email."

def main():
    print("User Login Validation")

    username = input("Enter Username: ")
    username_validation = validate_username(username)
    print(username_validation)
    if username_validation != "Valid username.":
        return

    password = input("Enter Password: ")
    password_validation = validate_password(password)
    print(password_validation)
    if password_validation != "Valid password.":
        return

    email = input("Enter Email: ")
    email_validation = validate_email(email)
    print(email_validation)
    if email_validation != "Valid email.":
        return

    print("All inputs are valid.")

if _name_ == "_main_":
    main()