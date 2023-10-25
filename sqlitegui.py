
import tkinter as tk
from tkinter import filedialog
import sqlite3

def open_database():
    global connection
    db_file = filedialog.askopenfilename(filetypes=[("Banco de Dados SQLite", "*.db *.sqlite")])
    if db_file:
        connection = sqlite3.connect(db_file)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Banco de Dados '{db_file}' aberto com sucesso.\n")

def execute_query():
    query = query_text.get("1.0", tk.END)
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        output_text.delete(1.0, tk.END)
        
        if query.strip().lower().startswith("select"):
            column_names = [description[0] for description in cursor.description]
            output_text.insert(tk.END, ", ".join(column_names) + "\n")
            
            for row in cursor.fetchall():
                output_text.insert(tk.END, ", ".join(map(str, row)) + "\n")
        else:
            output_text.insert(tk.END, "Consulta executada com sucesso.\n")
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Erro ao executar a consulta:\n")
        output_text.insert(tk.END, str(e) + "\n")

root = tk.Tk()
root.title("SQLite Query Executer")
root.configure(bg="brown", width=800, height=600)  # Define a cor de 
connection = None

open_button = tk.Button(root, text="Abrir Banco de Dados", command=open_database)
query_button = tk.Button(root, text="Executar Consulta", command=execute_query)

query_text = tk.Text(root, height=10, width=40)
output_text = tk.Text(root, height=10, width=40)

open_button.pack()
query_text.pack()
query_button.pack()
output_text.pack()

root.mainloop()
