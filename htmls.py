
import sys

def process_text(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            output_file.write("<html><head><title></title></head><body>")
            first_line = True

            for line in input_file:
                line = line.strip()

                if line.startswith("\\p "):
                    output_file.write("<p>" + line[3:] + "</p>\n")
                elif line.startswith("\\b "):
                    output_file.write("<b>" + line[3:] + "</b>\n")
                elif line.startswith("\\1 "):
                    output_file.write("<h1>" + line[3:] + "</h1>\n")
                elif line.startswith("\\2 "):
                    output_file.write("<h2>" + line[3:] + "</h2>\n")
                elif line.startswith("\\3 "):
                    output_file.write("<h3>" + line[3:] + "</h3>\n")
                elif line.startswith("\\4 "):
                    output_file.write("<h4>" + line[3:] + "</h4>\n")
                else:
                    if first_line:
                        output_file.write("<h1>" + line + "</h1>\n")
                        first_line = False
                    else:
                        output_file.write(line + "<br>\n")
                output_file.write("</body></html>")
        print(f"Arquivo HTML gerado com sucesso: {output_filename}")

    except FileNotFoundError:
        print("O arquivo de entrada não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python process_text.py <arquivo_de_entrada.txt> <arquivo_de_saida.html>")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        process_text(input_filename, output_filename)
