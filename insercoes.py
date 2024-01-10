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

    def carrega_evento_csv(self, arquivo):
        registros = arquivo.read()
        registros = registros.linesplit()
        
        for reg in registros:
            reg = reg.split(",")
            evento = Eventos(reg[0], reg[1], reg[2], reg[3])
            self.insere_evento(evento)

    def carrega_pessoa_csv(self, arquivo):
        registros = arquivo.read()
        registros = registros.linesplit()
        
        for reg in registros:
            reg = reg.split(",")
            pessoa = Pessoa(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7])
            self.insere_pessoa(pessoa)

    def carrega_premio_csv(self, arquivo):
        registros = arquivo.read()
        registros = registros.linesplit()
        
        for reg in registros:
            reg = reg.split(",")
            premio = Premio(reg[0], reg[1], reg[3], reg[4])
            self.insere_premio(premio)

    def carrega_nomiacao_csv(self, arquivo):
        registros = arquivo.read()
        registros = registros.linesplit()
        
        for reg in registros:
            reg = reg.split(",")
            nomiacao = ENominado(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
            self.insere_nomiacao(nomiacao)

    def carrega_filme_csv(self, arquivo):
        registros = arquivo.read()
        registros = registros.linesplit()
        
        for reg in registros:
            reg = reg.split(",")
            filme = Filme(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
            self.insere_filme(filme)

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
