import tkinter as tk
from tkinter import filedialog
import csv

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    if file_path:
        listbox.delete(0, tk.END)
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                listbox.insert(tk.END, row)

def update_item():
    selected_index = listbox.curselection()
    if selected_index:
        new_value = entry.get()
        listbox.delete(selected_index)
        listbox.insert(selected_index, new_value)
        entry.delete(0, tk.END)

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

def delete_item():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivos CSV", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for item in listbox.get(0, tk.END):
                csv_writer.writerow([item])

app = tk.Tk()
app.title("Editor de CSV")
app.configure(bg="brown", width=800, height=600)  # Define a cor de 

load_button = tk.Button(app, text="Carregar Arquivo", command=load_file)
save_button = tk.Button(app, text="Salvar para Arquivo", command=save_to_file)
listbox = tk.Listbox(app)
entry = tk.Entry(app)
update_button = tk.Button(app, text="Atualizar Item", command=update_item)
add_button = tk.Button(app, text="Adicionar Item", command=add_item)
delete_button = tk.Button(app, text="Apagar Item", command=delete_item)

load_button.pack()
listbox.pack()
entry.pack()
update_button.pack()
add_button.pack()
delete_button.pack()
save_button.pack()

app.mainloop()

