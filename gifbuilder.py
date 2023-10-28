
from PIL import Image
import os

def create_animated_gif(output_file):
    img_array = []
    frame_duration = 750  # Duração de cada frame em milissegundos

    i = 0
    while os.path.exists(f"{i}.bmp"):
        img = Image.open(f"{i}.bmp")
        img_array.append(img)
        i += 1

    img_array[0].save(output_file, save_all=True, append_images=img_array[1:], duration=frame_duration, loop=0)
    print(f"Arquivo GIF animado '{output_file}' criado com sucesso.")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    create_animated_gif("out.gif")
