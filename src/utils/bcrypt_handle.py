from bcrypt import checkpw, gensalt, hashpw

# Funcion para cifrar la contraseña
def encrypt(password: str) -> str:
    password_hashed = hashpw(password.encode('utf-8'), gensalt())
    return password_hashed.decode('utf-8')

# Funcion para verificar si la contraseña es correcta
def verified(password: str, password_hash: str) -> bool:
    is_valid = checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    return is_valid