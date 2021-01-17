#https://paulovitorweb.wordpress.com/2020/08/08/importando-tabela-do-postgresql-no-pandas/
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

import pandas as pd
import psycopg2 as pg

from sqlalchemy import false

host='localhost'
port='5432'
dbname='zanc'
user='postgres'
password='1234'
tbname = 'clientes'
connection = pg.connect("host='{}' port='{}' dbname='{}' user='{}' password='{}'"
                        .format(host, port, dbname, user, password))
df = pd.read_sql_query("select * from {}".format(tbname), con=connection)

df.info()

df.to_csv('clientes.csv', index=false)