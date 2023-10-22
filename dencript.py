import sys
from cryptography.fernet import Fernet

def decrypt_file(encrypted_file_path, key_path, output_file_path):
    with open(key_path, 'rb') as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(output_file_path, 'wb') as output_file:
        output_file.write(decrypted_data)

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 4:
        print("Uso: python decrypt_file.py <encrypted_file> <key_file> <output_file>")
    else:
        encrypted_file_path = sys.argv[1]
        key_file_path = sys.argv[2]
        output_file_path = sys.argv[3]
        decrypt_file(encrypted_file_path, key_file_path, output_file_path)
        print("Arquivo descriptografado com sucesso.")

