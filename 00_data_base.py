import sqlite3 as sq

# responsável pela conexão do banco de dados
conn = sq.connect('clientes.db')
# definição do cursos responsável pela navegação e manipulação dos registros no banco de dados
cursor = conn.cursor()

#criando uma tabela (schema)
cursor.execute("""
CREATE TABLE clientes (
    id        INTEGER      PRIMARY KEY AUTOINCREMENT
                           NOT NULL,
    nome      TEXT         NOT NULL,
    idade     INTEGER,
    cpf       VARCHAR (11) NOT NULL,
    email     TEXT         NOT NULL,
    fone      TEXT         NOT NULL,
    cidade    TEXT         NOT NULL,
    uf        VARCHAR (2)  NOT NULL,
    criado_em DATE         NOT NULL
);

""")
conn.commit()
print('Tabela criada com sucesso')
conn.close()