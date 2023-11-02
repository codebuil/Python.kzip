
import csv
import svgwrite
#pip install svgwrite
def converter_csv_para_svg(entrada_csv, saida_svg):
    # Cria um novo arquivo SVG
    dwg = svgwrite.Drawing(saida_svg, profile='full')

    with open(entrada_csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            if len(linha) == 4:
                x, y, x1, y1 = map(float, linha)

                # Adiciona uma linha no SVG com as coordenadas do arquivo CSV
                dwg.add(dwg.line(start=(x, y), end=(x1, y1), stroke=svgwrite.rgb(0, 0, 0)))

    # Salva o desenho vetorial no arquivo SVG
    dwg.save()

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    arquivo_entrada = "in.csv"
    arquivo_saida = "out.svg"
    converter_csv_para_svg(arquivo_entrada, arquivo_saida)
