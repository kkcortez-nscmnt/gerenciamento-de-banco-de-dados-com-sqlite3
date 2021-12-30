# update - alterando os dados
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

id_cliente = 1
novo_fone = '11-1000-2014'
noco_criado_em = '2021-30-11'

# alterando os dados da tabela
cursor.execute("""
UPDATE clientes
SET fone = ?, criado_em = ?
WHERE id = ?
""", (novo_fone, noco_criado_em, id_cliente))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()