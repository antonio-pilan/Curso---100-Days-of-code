import encoding

username = input("Username: ")
password = input("Password: ")
phase = 7

encoded_username= encoding.cipher_encoding(password=username, phase=phase)
encoded_password = encoding.cipher_encoding(password=password, phase=phase)


print(f"\nUser {encoded_username}\nPassword {encoded_password}")