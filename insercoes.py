import psycopg2 as pg
from entidades import *

class DataBase():
    def __init__(self, conn):
        self.connection = conn
        
    def executa_sql(self, sql):  
        cursor = self.connection.cursor()

        cursor.execute(sql)

        #self.connection.close()
    
    def insere_evento(self, evento):
        TABLE_NAME = 'tb_eventos'
        
        nome = evento.nome_evento
        tipo = evento.tipo
        nacionalidade = evento.nacionalidade
        ano_inicio = evento.ano_inicio
        
        
        sql = f''' INSERT INTO {TABLE_NAME}
                    VALUES ({nome}, {tipo}, {nacionalidade}, {ano_inicio}); '''
        
        print(sql)
        
        self.executa_sql(sql)
        
    def insere_edicao(self, edicao):
        TABLE_NAME = 'tb_edicao'
        
        localizacao = edicao.localizacao
        data_realizacao = edicao.data_realizacao
        nome_evento = edicao.nome_evento
        ano = edicao.ano
        
        sql = f''' INSERT INTO {TABLE_NAME} 
        VALUES ({localizacao}, {data_realizacao}, {nome_evento}, {ano}); '''
        
        print(sql)
        
        self.executa_sql(sql)
    
    def insere_premio(self, premio):
        nome_evento = premio.nome_evento
        ano = premio.ano
        tipo = premio.tipo
        nome_premio = premio.nome_premio

        sql = f''' INSERT INTO tb_premio
            VALUES ({nome_evento}, {ano}, {tipo}, {nome_premio}) '''
                            
        print(sql)
        
        self.executa_sql(sql)
      
    def insere_pessoa(self, pessoa):
        TABLE_NAME = 'tb_pessoa'

        nome_artistico = pessoa.nome_artistico
        nome_real = pessoa.nome_real
        sexo = pessoa.sexo
        ano_nasc = pessoa.ano_nascimento
        site = pessoa.site
        ano_inicio = pessoa.ano_inicio
        nro_total_anos = pessoa.total_anos
        situacao = pessoa.situacao
        
        sql = f''' INSERT INTO {TABLE_NAME} 
                    VALUES ({nome_artistico}, {nome_real}, {sexo}, {ano_nasc}, {site},
                            {ano_inicio}, {nro_total_anos}, {situacao}); '''
                            
        print(sql)
        
        self.executa_sql(sql)  
    
    def insere_jurado(self, jurado):
        TABLE_NAME = 'tb_jurado'
        
        id_jurado = jurado.id_jurado
        nome_evento = jurado.nome_evento
        ano = jurado.ano
        tipo = jurado.tipo
        nome_artistico = jurado.nome_artistico

        sql = f''' INSERT INTO {TABLE_NAME}
            VALUES ({id_jurado}, {nome_evento}, {ano}, {tipo}) '''
                            
        print(sql)
        
        self.executa_sql(sql)
    
    def insere_filme(self, filme):
        TABLE_NAME = 'tb_filmes'
        
        titulo_orig = filme.titulo_original
        ano = filme.ano_producao
        titulo_brasil = filme.titulo_no_brasil
        classe = filme.classe
        idioma_orig = filme.idioma_original
        arrec_prim_ano = filme.arrecadacao_prim_ano
    
    
        sql = f''' INSERT INTO {TABLE_NAME} 
                   VALUES ({titulo_orig}, {ano}, {titulo_brasil}, {classe},
                            {idioma_orig}, {arrec_prim_ano}); '''
                            
        print(sql)
        
        self.executa_sql(sql)
        
    def insere_documentario(self, documentario):
        TABLE_NAME = 'tb_documentarios'
        
        titulo_original = documentario.titulo_original
        ano_producao = documentario.ano_producao
    
        sql = f''' INSERT INTO {TABLE_NAME} 
                   VALUES ({titulo_original}, {ano_producao}); '''
                            
        print(sql)
        
        self.executa_sql(sql)
        
    def insere_outros(self, outros):
        TABLE_NAME = 'tb_outros'
        
        titulo_original = outros.titulo_original
        ano_producao = outros.ano_producao
    
        sql = f''' INSERT INTO {TABLE_NAME} 
                   VALUES ({titulo_original}, {ano_producao}); '''
                            
        print(sql)
        
        self.executa_sql(sql)        
        
    def insere_locais_estreia(self, locais_estreia):
        TABLE_NAME = 'tb_locais_estreia'
        
        id_estreia = locais_estreia.id_estreia
        titulo_original = locais_estreia.titulo_original
        ano_producao = locais_estreia.ano_producao
        
    
        sql = f''' INSERT INTO {TABLE_NAME} 
                   VALUES ({id_estreia}, {titulo_original}, {ano_producao}); '''
                            
        print(sql)
        
        self.executa_sql(sql)     

    def insere_indicados(self, indicados):
        TABLE_NAME = 'tb_indicados'
        
        id_indicacao = indicados.id_indicacao
        nome_evento = indicados.nome_evento
        ano = indicados.ano
        tipo = indicados.tipo
        titulo_original = indicados.titulo_original
        ano_producao = indicados.ano_producao
        nome_artistico = indicados.nome_artistico
        foi_vencedor = indicados.foi_vencedor
    
        sql = f''' INSERT INTO {TABLE_NAME} 
                   VALUES ({id_indicacao}, {nome_evento}, {ano}, {tipo}, {titulo_original}, 
                            {ano_producao}, {nome_artistico}, {foi_vencedor}); '''
                            
        print(sql)
        
        self.executa_sql(sql)     

    def insere_diretores(self, diretores):
        TABLE_NAME = 'tb_diretores'
        
        titulo_filme = diretores.titulo_filme
        ano_producao = diretores.ano_producao
        nome_artistico = diretores.nome_artistico
    
        sql = f''' INSERT INTO {TABLE_NAME} 
                   VALUES ({titulo_filme}, {ano_producao}, {nome_artistico}); '''
                            
        print(sql)
        
        self.executa_sql(sql)    

    def insere_produtores(self, produtores):
        TABLE_NAME = 'tb_produtores'
        
        titulo_filme = produtores.titulo_filme
        ano_producao = produtores.ano_producao
        nome_artistico = produtores.nome_artistico

        sql = f''' INSERT INTO {TABLE_NAME} 
                    VALUES ({titulo_filme}, {ano_producao}, {nome_artistico}); '''
                            
        print(sql)
        
        self.executa_sql(sql)    
        
    def insere_roteiristas(self, roteiristas):
        TABLE_NAME = 'tb_roteiristas'
        
        titulo_filme = roteiristas.titulo_filme
        ano_producao = roteiristas.ano_producao
        nome_artistico = roteiristas.nome_artistico

        sql = f''' INSERT INTO {TABLE_NAME} 
                    VALUES ({titulo_filme}, {ano_producao}, {nome_artistico}); '''
                            
        print(sql)
        
        self.executa_sql(sql) 
        
    def insere_ator_principal(self, ator_principal):
        TABLE_NAME = 'tb_ator_principal'
        
        titulo_filme = ator_principal.titulo_filme
        ano_producao = ator_principal.ano_producao
        nome_artistico = ator_principal.nome_artistico

        sql = f''' INSERT INTO {TABLE_NAME} 
                    VALUES ({titulo_filme}, {ano_producao}, {nome_artistico}); '''
                            
        print(sql)
        
        self.executa_sql(sql) 
        
    def insere_ator_elenco(self, ator_elenco):
        TABLE_NAME = 'tb_ator_elenco'
        
        titulo_filme = ator_elenco.titulo_filme
        ano_producao = ator_elenco.ano_producao
        nome_artistico = ator_elenco.nome_artistico

        sql = f''' INSERT INTO {TABLE_NAME} 
                    VALUES ({titulo_filme}, {ano_producao}, {nome_artistico}); '''
                            
        print(sql)
        
        self.executa_sql(sql) 