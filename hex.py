import sys

def hexdump(filename, start_offset):
    try:
        with open(filename, 'rb') as file:
            file.seek(start_offset)
            line_count = 0
            while line_count < 17:
                data = file.read(16)
                if not data:
                    break
                
                hex_string = ', '.join(f'{byte:02X}' for byte in data)
                char_string = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in data)
                
                print(f"{hex_string}, {char_string}")
                line_count += 1
    except FileNotFoundError:
        print("O arquivo especificado não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    if len(sys.argv) != 3:
        print("Uso: python hexdump.py <nome_do_arquivo> <offset>")
    else:
        filename = sys.argv[1]
        start_offset = int(sys.argv[2])
        hexdump(filename, start_offset)

