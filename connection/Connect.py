import psycopg2
# https://pt.wikibooks.org/wiki/PostgreSQL_Pr%C3%A1tico/Ferramentas/psql

conn = psycopg2.connect(database="zanc", user="postgres", password="1234")

cursor = conn.cursor()
cursor.execute("create table test (id serial primary key, num integer, dados varchar(50));")
cursor.execute("insert into test(num, dados) values(%s, %s)",
               (15,"Testando"))
cursor.execute("select * from test")
linha = cursor.fetchone()
linha
cursor.close()
conn.close()



'''
class Connection(object):
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect_postgres(self,client_encoding='utf8'):
        conn = psycopg2.connect(
            host = 'localhost:5432',
            database = 'zanc',
            user = 'postgres',
            password = '1234',
             client_encoding=client_encoding
        )
        return conn
'''
