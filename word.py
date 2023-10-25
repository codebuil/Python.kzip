import sys
import os

import win32com.client as win32
#pip install pywin32
def create_word_document(output_filename,in_file):
    word = win32.gencache.EnsureDispatch("Word.Application")
    doc = word.Documents.Add()
    doc.Content.Text = in_file
    doc.SaveAs(output_filename, 0)
    doc.Close()
    word.Quit()

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")
    lists=""
    if len(sys.argv) != 3:
        print("Uso: python create_word_document.py <in.txt> <arquivo_de_saida.doc>")
    else:
        output_filename = sys.argv[2]
    try:
        with open(sys.argv[1], 'r') as input_file:
            lists=input_file.read()
        if output_filename.lower().endswith('.doc'):
            create_word_document(os.getcwd()+"\\"+output_filename,lists)
            print(f"Arquivo Word gerado com sucesso: {output_filename}")
        else:
            print("O nome do arquivo de saída deve ter a extensão .doc")

    except FileNotFoundError:
        print("O arquivo de entrada não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")