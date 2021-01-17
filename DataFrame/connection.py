import sqlite3
'''
http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#criando-um-banco-de-dados
# Create a SQL connection to our SQLite database
con = sqlite3.connect('ZancFake.db')

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM test;'):
    print(row)

# Be sure to close the connection
con.close() '''
# conectando...
conn = sqlite3.connect('zanc.db')
# definindo um cursor
cursor = conn.cursor()
'''
# criando a tabela (schema)
cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,clientes
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...

'''
# lendo os dados
cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()