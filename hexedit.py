import sys
import csv

def hexedit(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            with open(output_filename, 'wb') as output_file:
                for row in reader:
                    for hex_value in row:
                        if len(hex_value)>1:
                             
                             binary_data = bytes.fromhex(hex_value)
                             output_file.write(binary_data)
                             
    except FileNotFoundError:
        print("O arquivo de entrada não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python hexedit.py <arquivo_de_entrada.csv> <arquivo_de_saida>")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        hexedit(input_filename, output_filename)
