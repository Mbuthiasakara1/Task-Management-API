from flask_bcrypt import generate_password_hash,check_password_hash


def hash_password(password):
    """
    convert plain text and return hashed version
    
    """

    return generate_password_hash(password).decode('utf-8')


def verify_password(plain_password, hashed_password):
    """
    compares a plain text password with a hashed password
   
    """

    return check_password_hash(hashed_password,plain_password)