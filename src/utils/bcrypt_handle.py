from bcrypt import check_pw, gensalt, hash_pw

# Funcion para cifrar la contraseña
def encrypt(password: str) -> str:
    password_hashed = hash_pw(password.encode('utf-8'), gensalt())
    return password_hashed.decode('utf-8')

# Funcion para verificar si la contraseña es correcta
def verified(password: str, password_hash: str) -> bool:
    is_valid = check_pw(password.encode('utf-8'), password_hash.encode('utf-8'))
    return is_valid