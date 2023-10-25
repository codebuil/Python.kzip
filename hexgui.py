
import tkinter as tk
from tkinter import filedialog

def hexdump_file(filename, start_offset):
    try:
        with open(filename, 'rb') as file:
            file.seek(start_offset)
            result = []
            for _ in range(17):
                data = file.read(16)
                if not data:
                    break
                hex_string = ', '.join(f'{byte:02X}' for byte in data)
                char_string = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in data)
                result.append(f"{hex_string}, {char_string}")
            return '\n'.join(result)
    except FileNotFoundError:
        return "O arquivo especificado não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Todos os arquivos", "*.*")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def display_hexdump():
    filename = file_entry.get()
    start_offset = int(offset_entry.get())
    hexdump_text.delete(1.0, tk.END)
    result = hexdump_file(filename, start_offset)
    hexdump_text.insert(tk.END, result)

app = tk.Tk()
app.title("Hexdump Viewer")
app.configure(bg="brown", width=800, height=600)  # Define a cor de 
file_label = tk.Label(app, text="Nome do Arquivo:")
file_entry = tk.Entry(app)
offset_label = tk.Label(app, text="Offset de Início:")
offset_entry = tk.Entry(app)
open_button = tk.Button(app, text="Selecionar Arquivo", command=open_file)
display_button = tk.Button(app, text="Exibir Hexdump", command=display_hexdump)
hexdump_text = tk.Text(app, height=17, width=80, font=("Courier New", 10))

file_label.pack()
file_entry.pack()
offset_label.pack()
offset_entry.pack()
open_button.pack()
display_button.pack()
hexdump_text.pack()

app.mainloop()
