from insercoes import *

def carregamento_pessoas(arquivo, db):
    
    arquivo = open(arquivo,  'r')
    arquivo = arquivo.read()
    
    linhas = arquivo.split('\n')
    
    for linha in linhas:
        linha = linha[1:-1]
        linha = linha.split(',')
        linha = [i.strip() for i in  linha]
        pessoa = Pessoa(linha[0], linha[1], linha[2], int(linha[3]), linha[4], int(linha[5]), int(linha[6]), linha[7])
        db.insere_pessoa(pessoa)
        
def carregamento_eventos(arquivo, db):
    
    arquivo = open(arquivo,  'r')
    arquivo = arquivo.read()
    
    linhas = arquivo.split('\n')
    
    for linha in linhas:
        linha = linha[1:-1]
        linha = linha.split(',')
        linha = [i.strip() for i in  linha]
        evento = Eventos(linha[0], linha[1], linha[2], int(linha[3]))
        db.insere_evento(evento)
        
def carregamento_edicao_eventos(arquivo, db):
    
    arquivo = open(arquivo,  'r')
    arquivo = arquivo.read()
    
    linhas = arquivo.split('\n')
    
    for linha in linhas:
        linha = linha[1:-1]
        linha = linha.split(',')
        linha = [i.strip() for i in  linha]
        edicao = Edicao(linha[0], linha[1], linha[2], int(linha[3]))
        db.insere_edicao(edicao)

def carregamento_filmes(arquivo, db):
    
    arquivo = open(arquivo,  'r')
    arquivo = arquivo.read()
    
    linhas = arquivo.split('\n')
    
    for linha in linhas:
        linha = linha[1:-1]
        linha = linha.split(',')
        linha = [i.strip() for i in  linha]
        filme = Filme(linha[0], int(linha[1]), linha[2], linha[3], linha[4], int(linha[5]))
        db.insere_filme(filme)
        
def carregamento_locais_estreia(arquivo, db):
    
    arquivo = open(arquivo,  'r')
    arquivo = arquivo.read()
    
    linhas = arquivo.split('\n')
    
    for linha in linhas:
        linha = linha[1:-1]
        linha = linha.split(',')
        linha = [i.strip() for i in  linha]
        locais = LocaisEstreia(int(linha[0]), linha[1], linha[2], linha[3])
        db.insere_locais_estreia(locais)
        
def carregamento_premios(arquivo, db):
    
    arquivo = open(arquivo,  'r')
    arquivo = arquivo.read()
    
    linhas = arquivo.split('\n')
    
    for linha in linhas:
        linha = linha[1:-1]
        linha = linha.split(',')
        linha = [i.strip() for i in  linha]
        premio = Premio(linha[0], int(linha[1]), linha[2], linha[3])
        db.insere_premio(premio)

def carregamento_indicacoes(arquivo, db):
    
    arquivo = open(arquivo,  'r')
    arquivo = arquivo.read()
    
    linhas = arquivo.split('\n')
    
    for linha in linhas:
        linha = linha[1:-1]
        linha = linha.split(',')
        linha = [i.strip() for i in  linha]
        indicacao = Indicados(int(linha[0]), linha[1], int(linha[2]), linha[3], linha[4], int(linha[5]), linha[6], linha[7])
        db_filmes.insere_indicados(indicacao)
        
        
conn = pg.connect(
    database='filmes',
    user='postgres',
    password='1234',
    host='localhost',
    port='5434'
)

db_filmes = DataBase(conn)

conn.autocommit = True

carregamento_pessoas('arquivos_carregamento\\pessoa.txt', db_filmes)
carregamento_eventos('arquivos_carregamento\\eventos.txt', db_filmes)
carregamento_edicao_eventos('arquivos_carregamento\\edicao_evento.txt', db_filmes)
carregamento_filmes('arquivos_carregamento\\filmes.txt', db_filmes)
carregamento_locais_estreia('arquivos_carregamento\\locais_estreia.txt', db_filmes)
carregamento_premios('arquivos_carregamento\\premios.txt', db_filmes)
carregamento_indicacoes('arquivos_carregamento\\indicacoes.txt', db_filmes)

conn.close()