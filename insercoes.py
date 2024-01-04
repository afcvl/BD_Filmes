import psycopg2 as pg
from entidades import *

class DataBase():
    def __init__(self, conn):
        self.connection = conn
        
    def executa_sql(self, sql):  
        cursor = self.connection.cursor()

        cursor.execute(sql)

        self.connection.close()
        
 
    def insere_evento(self, evento):
        nome = evento.nome_evento
        ano_inicio = evento.ano_inicio
        tipo = evento.tipo
        nacionalidade = evento.nacionalidade
        
        
        sql = f''' INSERT INTO tb_eventos VALUES ('{nome}', {ano_inicio}, '{tipo}', '{nacionalidade}'); '''
        
        print(sql)
        
        self.executa_sql(sql)
        
        
    def insere_pessoa(self, pessoa):
        pass

    def insere_premio(self):
        pass
    
    def insere_nomiacao(self):
        pass
    
    def insere_premiacao(self):
        pass
    
    def insere_filme(self):
        pass
        

     
conn = pg.connect(
   database="filmes",
    user='postgres',
    password='1234',
    host='localhost',
    port= '5434'
)
        
db = DataBase(conn)

evento = Eventos('oscar', '2010', 'filme','jamaica')

db.insere_evento(evento)