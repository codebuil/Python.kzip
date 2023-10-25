import sys
import pandas as pd
# pip install openpyxl
def csv_to_excel(input_file, output_file):
    try:
        data = pd.read_csv(input_file)
        data.to_excel(output_file, index=False)

        print(f"Arquivo Excel gerado com sucesso: {output_file}")

    except FileNotFoundError:
        print("O arquivo de entrada não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python csv_to_excel.py <arquivo_de_entrada.csv> <arquivo_de_saida.xlsx>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        if input_file.lower().endswith('.csv') and output_file.lower().endswith('.xlsx'):
            csv_to_excel(input_file, output_file)
        else:
            print("Certifique-se de que o arquivo de entrada seja CSV e o arquivo de saída seja XLSX.")

