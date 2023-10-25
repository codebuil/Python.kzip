import sys

def process_text(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            first_line = True

            output_file.write("{\\rtf1\\ansi\\deff0\n")  # Cabeçalho RTF

            for line in input_file:
                line = line.strip()

                if line.startswith("\\p "):
                    output_file.write("{\\par " + line[3:] + "\\par}\n")
                elif line.startswith("\\b "):
                    output_file.write("{\\b " + line[3:] + "\\b0}\n")
                elif line.startswith("\\1 "):
                    output_file.write("{\\fs48 " + line[3:] + "\\fs40}\n")  # Tamanho da fonte 48
                elif line.startswith("\\2 "):
                    output_file.write("{\\fs36 " + line[3:] + "\\fs40}\n")  # Tamanho da fonte 36
                elif line.startswith("\\3 "):
                    output_file.write("{\\fs28 " + line[3:] + "\\fs40}\n")  # Tamanho da fonte 28
                elif line.startswith("\\4 "):
                    output_file.write("{\\fs24 " + line[3:] + "\\fs40}\n")  # Tamanho da fonte 24
                else:
                    if first_line:
                        output_file.write("{\\fs48 " + line + "\\fs40\\par}\n")  # Tamanho da fonte 48
                        first_line = False
                    else:
                        output_file.write("{\\par " + line + "\\par}\n")

            output_file.write("}\n")  # Rodapé RTF

        print(f"Arquivo RTF gerado com sucesso: {output_filename}")

    except FileNotFoundError:
        print("O arquivo de entrada não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python process_text_rtf.py <arquivo_de_entrada.txt> <arquivo_de_saida.rtf>")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        process_text(input_filename, output_filename)

