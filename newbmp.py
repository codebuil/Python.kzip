from PIL import Image
import sys

def create_colored_bmp(filename, width, height, color_index):
    try:
        # Verifica se o índice da cor está no intervalo válido (0-15)
        if 0 <= color_index <= 15:
            # Mapeia o índice da cor para um valor RGB VGA de 16 cores
            vga_colors = [
                (0, 0, 0), (0, 0, 170), (0, 170, 0), (0, 170, 170),
                (170, 0, 0), (170, 0, 170), (170, 85, 0), (170, 170, 170),
                (85, 85, 85), (85, 85, 255), (85, 255, 85), (85, 255, 255),
                (255, 85, 85), (255, 85, 255), (255, 255, 85), (255, 255, 255)
            ]

            # Cria uma imagem em branco com as dimensões especificadas
            image = Image.new("RGB", (width, height), vga_colors[color_index])

            # Salva a imagem como um arquivo BMP de 24 bits
            image.save(filename, "BMP")

            print(f"Arquivo BMP criado com sucesso: {filename}")
        else:
            print("O índice de cor deve estar no intervalo de 0 a 15.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 5:
        print("Uso: python create_colored_bmp.py <nome_do_arquivo.bmp> <largura> <altura> <indice_de_cor>")
    else:
        output_filename = sys.argv[1]
        width = int(sys.argv[2])
        height = int(sys.argv[3])
        color_index = int(sys.argv[4])
        create_colored_bmp(output_filename, width, height, color_index)

