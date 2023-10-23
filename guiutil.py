import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from cryptography.fernet import Fernet
import zlib
import struct

def encrypt_file():
    file_path = filedialog.askopenfilename(title="Selecione o arquivo a ser criptografado")
    if file_path:
        password = password_entry.get()
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

        messagebox.showinfo("Sucesso", "Arquivo criptografado com sucesso.")

def decrypt_file():
    file_path = filedialog.askopenfilename(title="Selecione o arquivo a ser descriptografado")
    key_file_path = filedialog.askopenfilename(title="Selecione o arquivo key")
    if file_path:
        try:
            with open(key_file_path, 'rb') as key_file:
                key = key_file.read()

            cipher_suite = Fernet(key)

            with open(file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            decrypted_data = cipher_suite.decrypt(encrypted_data)

            output_file_path = filedialog.asksaveasfilename(title="Salve o arquivo descriptografado", defaultextension=".txt")
            if output_file_path:
                with open(output_file_path, 'wb') as output_file:
                    output_file.write(decrypted_data)

                messagebox.showinfo("Sucesso", "Arquivo descriptografado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", "Falha ao descriptografar o arquivo. Verifique a chave.")

def compress_file():
    file_path = filedialog.askopenfilename(title="Selecione o arquivo a ser comprimido")
    if file_path:
        with open(file_path, 'rb') as in_file:
            data = in_file.read()

        compressed_data = zlib.compress(data)

        output_file_path = filedialog.asksaveasfilename(title="Salve o arquivo comprimido", defaultextension=".zlib")
        if output_file_path:
            with open(output_file_path, 'wb') as out_file:
                out_file.write(compressed_data)

        messagebox.showinfo("Sucesso", "Arquivo comprimido com sucesso.")

def decompress_file():
    file_path = filedialog.askopenfilename(title="Selecione o arquivo a ser descomprimido")
    if file_path:
        with open(file_path, 'rb') as in_file:
            compressed_data = in_file.read()

        decompressed_data = zlib.decompress(compressed_data)

        output_file_path = filedialog.asksaveasfilename(title="Salve o arquivo descomprimido", defaultextension=".txt")
        if output_file_path:
            with open(output_file_path, 'wb') as out_file:
                out_file.write(decompressed_data)

        messagebox.showinfo("Sucesso", "Arquivo descomprimido com sucesso.")

def extract_files():
    packed_file = filedialog.askopenfilename(title="Selecione o arquivo empacotado")
    output_directory = filedialog.askdirectory(title="Selecione o diretório de saída")
    with open(packed_file, 'rb') as pak_file:
        # Leitura do deslocamento da lista a partir do final do arquivo
        pak_file.seek(-struct.calcsize('Q'), 2)
        list_offset = struct.unpack('Q', pak_file.read(struct.calcsize('Q')))[0]

        # Lê a lista de arquivos a partir do deslocamento
        pak_file.seek(list_offset)
        list_data = pak_file.read()
        list_entries = list_data.decode('utf-8').split('\n')

        for i in range(len(list_entries)):
            entry = list_entries[i]
            if entry:
                entrys = entry.split(',')
                if len(entrys) > 1:
                    file_name = entrys[0]
                    start_offset = int(entrys[1])

                    # Calcula o tamanho do arquivo atual com base no próximo arquivo na lista
                    if i < len(list_entries) - 2:
                        
                        next_entry = list_entries[i + 1]
                        next_start_offset = int(next_entry.split(',')[1])
                        file_size = next_start_offset - start_offset
                    else:
                        # No último arquivo, extrai até o início do arquivo "list.txt"
                        pak_file.seek(0)
                        file_size = list_offset - start_offset

                    # Lê o conteúdo do arquivo do pacote
                    pak_file.seek(start_offset)
                    file_data = pak_file.read(file_size)

                    # Escreve o arquivo descompactado
                    with open(f"{output_directory}/{file_name}", 'wb') as output_file:
                        output_file.write(file_data)


# Configuração da janela principal
root = tk.Tk()
root.title("Utilitário de Criptografia e Compactação")
root.configure(bg="brown", width=800, height=600)  # Define a cor de fundo da janela 


# Criação de widgets
password_label = tk.Label(root, text="Senha:")
password_entry = tk.Entry(root, show="*")
encrypt_button = tk.Button(root, text="Criptografar Arquivo", command=encrypt_file)
decrypt_button = tk.Button(root, text="Descriptografar Arquivo", command=decrypt_file)
compress_button = tk.Button(root, text="Comprimir Arquivo", command=compress_file)
decompress_button = tk.Button(root, text="Descomprimir Arquivo", command=decompress_file)
extract_button = tk.Button(root, text="Extrair Arquivos", command=extract_files)

# Layout dos widgets
password_label.pack()
password_entry.pack()
encrypt_button.pack()
decrypt_button.pack()
compress_button.pack()
decompress_button.pack()
extract_button.pack()

root.mainloop()
