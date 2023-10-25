
import sys

def create_and_write_file(filename):
    try:
        with open(filename, 'w') as file:
            print(f"Digite o conteúdo do arquivo '{filename}'. Pressione Enter em uma linha em branco para finalizar.")
            while True:
                line = input()
                if not line:
                    break
                file.write(line + '\n')
        print(f"Arquivo '{filename}' criado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 2:
        print("Uso: python create_file.py <nome_do_arquivo>")
    else:
        filename = sys.argv[1]
        create_and_write_file(filename)
