# inserindo uma nova coluna com o comando SQL ALTER TABLE
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# adicionando uma nova colunana tabela clientes
cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")

conn.commit()

print("Novo campo adicionado com sucesso.")

conn.close()