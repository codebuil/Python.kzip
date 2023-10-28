import sys

def display_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # Imprime o número de linha formatado com 5 dígitos e o conteúdo da linha
                print(f"{i:5} {line.strip()}")  # Utiliza strip() para remover espaços em branco e quebras de linha

    except FileNotFoundError:
        print("O arquivo não pôde ser encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 2:
        print("Uso: python display_file_content.py <nome_do_arquivo>")
    else:
        file_name = sys.argv[1]
        display_file_content(file_name)

