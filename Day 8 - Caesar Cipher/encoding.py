def cipher_encoding(password, phase):
    encoded = "".join(chr(ord(charact)+phase) for charact in password)
    return encoded