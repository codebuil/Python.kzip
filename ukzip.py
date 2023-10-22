
import sys
import zlib

def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as in_file:
        compressed_data = in_file.read()

    decompressed_data = zlib.decompress(compressed_data)

    with open(output_file, 'wb') as out_file:
        out_file.write(decompressed_data)

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python decompress_file.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        decompress_file(input_file, output_file)
