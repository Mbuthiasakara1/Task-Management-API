import re


def is_valid_email(email):
    """
    Validates email format using regex
    """

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern,email):
        return True
    return False


def is_strong_password(password):
    """
   checks if password meets strendth requirements:
   -atleast 8 characters
   -contains atleast one uppercase letter
   -contains at least one lowercase letter
   -contains at least one number
    """

    if len(password) < 8:
        return False ,"Password must be at least 8 characters long"
    
    if not re.search(r'[A-Z]',password):
        return False ,"Password must contain at least one uppercase letter"
    
    if not re.search(r'[a-z]',password):
        return False ,"Password must contain at least one lower case letter"
    
    if not re.search(r'[0-9]',password):
        return False,"Password must contain atleast one number"
    
    return True, "Passsword is strong"