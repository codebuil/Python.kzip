import sys
import zlib

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as in_file:
        data = in_file.read()

    compressed_data = zlib.compress(data)

    with open(output_file, 'wb') as out_file:
        out_file.write(compressed_data)

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python compress_file.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        compress_file(input_file, output_file)
