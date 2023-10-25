import sqlite3

def create_database(db_name):
    connection = sqlite3.connect(db_name)
    connection.close()

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    
    if query.strip().lower().startswith("select"):
        column_names = [description[0] for description in cursor.description]
        print(", ".join(column_names))
        
        for row in cursor.fetchall():
            print(", ".join(map(str, row)))

def main():
    db_name = input("Digite o nome do banco de dados: ")
    create_database(db_name)

    connection = sqlite3.connect(db_name)

    print("Bem-vindo ao SQLite. Digite suas consultas ou deixe vazio para sair.")
    while True:
        query = input("sqlite> ")
        if not query:
            break
        execute_query(connection, query)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")
    main()

