import sqlite3
from sqlite3.dbapi2 import Cursor

# inserção de dados em uma tabela por meio de tuplas
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# cridando uma lista de dados
lista =[
    ('Fabio', 23, '44444444444', 'fabio@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2014-06-09'),
    ('João', 21, '55555555555', 'Joao@email.com', '11-1234-5600', 'São Paulo', 'SP', '2014-09-09'),
    ('Xavier', 24, '66666666666', 'xavier@gmail.com', '12-1234-5601','Campinas', 'SP', '2014-06-10')
    ]

# inserindo dados na tabela
cursor.executemany("""
INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES(?,?,?,?,?,?,?,?)
""", lista)

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()