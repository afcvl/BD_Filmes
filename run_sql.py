from sqlalchemy import create_engine
import psycopg2 as pg

conn = pg.connect(
   database="postgres",
    user='postgres',
    password='1234',
    host='localhost',
    port= '5434'
)

conn.autocommit = True
 
# Creating a cursor object
cursor = conn.cursor()
 
# query to create a database 
sql = ''' DROP DATABASE filmes; '''
 
# executing above query
cursor.execute(sql)

conn.close()



