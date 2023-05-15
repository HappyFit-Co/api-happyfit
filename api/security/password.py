import bcrypt


def encrypt_pwd(pwd):
    hashed_password = bcrypt.hashpw(pwd.encode(
        'utf-8'), bcrypt.gensalt()).decode('utf-8')
    return hashed_password


def compare_pwd(pwd, hash_pwd):
    return bcrypt.checkpw(pwd.encode('utf-8'), hash_pwd.encode('utf-8'))
