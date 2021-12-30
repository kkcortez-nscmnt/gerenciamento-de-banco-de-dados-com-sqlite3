# read - lendo os dados com SELECT e método fetchall(), que é reponsavel pelo retorno do select
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()


# lendo os dados
cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()