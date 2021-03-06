import sqlite3
from sqlite3.dbapi2 import Cursor
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# inserção de dados em uma tabela da base de dados

cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-06-08');
    """)

cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com', '98765-4322', 'Porto Alegre', 'RS', '2014-06-09');
    """)

cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Bruna', 21, '22222222222', 'bruna@gmail.com', '21-98765-4323', 'Rio de Janeiro', 'RJ', '2014-06-09');
    """)

cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Matheus', 19, '33333333333', 'matheus@gmail.com', '11-98765-4324', 'Campinas', 'SP', '2014-06-08');
    """)

# gravando no banco de dados
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()