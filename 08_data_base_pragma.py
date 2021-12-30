# lendo informações do banco de dados
# para listar tabelas do banco  usamos o comando SELECT name FROM sqlite_master...
# paea lero schema da tabela usamos o comando SELECT sql FROM sqliter_master...

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
nome_tabela = 'clientes'


# obtendo informações da tabela
cursor.execute('PRAGMA table_info({})'.format(nome_tabela))

colunas = [tupla[1] for tupla in cursor.fetchall()]
print('Colunas: ', colunas)

# ou
# for coluna in colunas:
#   print(coluna)

# listando as tabelas do bd
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print('Tabelas: ')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

# obtendo o schema da tabela
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=? 
""", (nome_tabela,))

print('Schema: ')
for schema in cursor.fetchall():
    print("%s" % (schema))

conn.close()