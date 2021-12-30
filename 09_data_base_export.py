# fazendo backup do banco de dados(exportando dados)

# biblioteca io salva os dados em um arquivo extrerno através do método write.
# o método interdump() exporta a estrutura e dados da tabela para o arquivo externo.

import sqlite3
import io

conn = sqlite3.connect('clientes.db')

with io.open('clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)

print('Backup realizado com sucesso.')
print('Salvo como clientes_dump.sql')

conn.close()