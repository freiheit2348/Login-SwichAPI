# login.py
from registered_users import registered_users

def login(username, password):
    if username in registered_users and registered_users[username] == password:
        return True, "Login successful!"
    else:
        return False, "Invalid username or password."