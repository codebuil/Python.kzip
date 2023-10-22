import sys
from cryptography.fernet import Fernet
#pip install cryptography

def encrypt_file(file_path, password):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = cipher_suite.encrypt(data)

    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    with open(file_path + ".key", 'wb') as key_file:
        key_file.write(key)

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python encrypt_file.py <file_path> <password>")
    else:
        file_path = sys.argv[1]
        password = sys.argv[2]
        encrypt_file(file_path, password)
        print("Arquivo criptografado com sucesso.")

