import re

def is_login_data_valid(username, password):
    if len(password) < 6 or len(password) > 30:
        return False
    if not re.match(r"^[\w]{3,20}$", username): # if is made of alphanumerical characters
        return False
    return True
