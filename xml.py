import csv
import xml.etree.ElementTree as ET
import sys

def csv_to_xml(input_file, output_file):
    try:
        with open(input_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            root = ET.Element("data")

            for row in csv_reader:
                item = ET.SubElement(root, "item")
                for key, value in row.items():
                    sub_element = ET.SubElement(item, key)
                    sub_element.text = value

            tree = ET.ElementTree(root)
            tree.write(output_file, encoding='utf-8', xml_declaration=True)

        print(f"Arquivo XML gerado com sucesso: {output_file}")

    except FileNotFoundError:
        print("O arquivo de entrada não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python csv_to_xml.py <arquivo_de_entrada.csv> <arquivo_de_saida.xml>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        if input_file.lower().endswith('.csv') and output_file.lower().endswith('.xml'):
            csv_to_xml(input_file, output_file)
        else:
            print("Certifique-se de que o arquivo de entrada seja CSV e o arquivo de saída seja XML.")

