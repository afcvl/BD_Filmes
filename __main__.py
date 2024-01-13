from metodos.tabelas import * 
from metodos.insercoes import *
from sqlalchemy import create_engine
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def menu_principal(db_filmes):
    
    while True:
        print("1. Cadastrar registros manualmente")
        print("2. Gerar grafico com os 10 autores com maior numero de premios")
        print("3. Gerar grafico com os 10 filmes mais premiados")
        print("4. Gerar grafico com os 10 filmes de maior arrecadacao")
        print("5. Listar os atores nominados como melhor ator em todos os eventos existentes")
        print("6. Dado um premio, pesquisar quais autores ou filmes foram nominados e premiados")
        print("7. Sair")
        opcao = input("Digite a sua opcao: ")
        match opcao:
            case "1":
                menu_cadastro(db_filmes)
            case "2":
                grafico1(db_filmes.connection)
            case "3":
                grafico2(db_filmes.connection)
            case "4":
                grafico3(db_filmes.connection)
            case "5":
                lista_melhores_atores(db_filmes.connection)
            case "6":
                print("Escolha um premio no formato: 'nome_premio', ano, 'tipo'")
                print("Exemplo: 'Oscar', 2018, 'Melhor Ator'")
                
                premio = input('premio: ')
                premio = premio.split(",")
                premio = [i.strip() for i in  premio]
                premio = Premio(premio[0], premio[1], premio[2], '')
                
                indicados_do_premio(db_filmes.connection, premio)
                
            case "7":
                exit()

def menu_cadastro(db_filmes):
    while True:
        print("O que deseja cadastrar?")
        print("1. Pessoas")
        print("2. Eventos")
        print("3. Edicao de evento")
        print("4. Premios")
        print("5. Filmes")        
        print("6. Indicações")
        print("7. Menu principal")
        print("8. Sair")

        try:
            opcao = input("Digite a sua opcao: ")
        except:
            print("\nERRO: Opcao invalida\n")
            continue

        match opcao:
            case "1": # pessoa
                print("Digite as informacoes da pessoa no formato: 'nome_artistico', 'nome_real', 'sexo', ano_nascimento, 'site', ano_inicio, total_anos, 'situacao'") 
                print("Exemplo: ('Johnny Depp', 'John Christopher Depp II', 'Masculino', 1963, 'WWW.jdepp.com', 1984, 38, 'Vivo')"),
                try:
                    reg = input()
                    reg = reg.split(",")
                    reg = [i.strip() for i in  reg]
                    pessoa = Pessoa(reg[0], reg[1], reg[2], int(reg[3]), reg[4], int(reg[5]), int(reg[6]), reg[7])
                    db_filmes.insere_pessoa(pessoa)
                except:
                    print("\nERRo: Registro invalido, siga a formatacao correta: 'nome_artistico', 'nome_real', 'sexo', ano_nascimento, 'site', ano_inicio, total_anos, 'situacao'\n")
                    continue

            case "2": # evento
                print("Digite as informacoes do evento no formato: 'nome_evento','tipo', 'nacionalidade', ano_inicio")
                print("Exemplo: 'Oscar', 'Premiacao', 'Americano', 1929\n")
                try:
                    reg = input()
                    reg = reg.split(",")
                    reg = [i.strip() for i in  reg]
                    evento = Eventos(reg[0], reg[1], reg[2], int(reg[3]))
                    db_filmes.insere_evento(evento)
                except:
                    print("\nERRO: Registro invalido, siga a formatacao correta: 'nome_evento','tipo', 'nacionalidade', ano_inicio\n")
                    continue 

                flag = input('deseja inserir uma edição do evento? S/N: ')
                print()
                if flag.upper() == 'S':
                    print("Digite as informacoes da edicao no formato: 'localizacao','data_realizacao', 'nome_evento', ano")
                    print("Exemplo: 'Nova York', '05-05-2020', 'Oscar', 2020")
                    print(f"Lembre-se que o evento deve ser '{reg[0]}'")
                    try:
                        reg = input()
                        reg = reg.split(",")
                        reg = [i.strip() for i in  reg]
                        edicao = Edicao(reg[0], reg[1], reg[2], int(reg[3]))
                        db_filmes.insere_edicao(edicao)
                    except:
                        print("\nERRO: Registro invalido, siga a formatacao correta: 'localizacao','data_realizacao', 'nome_evento', ano\n")
                        print(f"Lembre-se que o evento deve ser '{reg[0]}'")
                        continue 

            case "3": # edição
                print("Digite as informacoes da edicao no formato: 'localizacao','data_realizacao', 'nome_evento', ano")
                print("Exemplo: 'Nova York', '05-05-2020', 'Oscar', 2020")
                print(f'Lembre-se de utilizar o nome de um evento existente"')
                try:
                    reg = input()
                    reg = reg.split(",")
                    reg = [i.strip() for i in  reg]
                    edicao = Edicao(reg[0], reg[1], reg[2], int(reg[3]))
                    db_filmes.insere_edicao(edicao)
                except:
                    print("\nERRO: Registro invalido, siga a formatacao correta: 'localizacao','data_realizacao', 'nome_evento', 'ano'\n")
                    continue 

            case "4": # premio
                print("Digite as informacoes do premio no formato: 'nome_evento', ano, 'tipo', 'nome_premio'")
                print("Exemplo: 'Oscar', 2020, 'Melhor Ator', 'Oscar'")
                try:
                    reg = input()
                    reg = reg.split(",")
                    reg = [i.strip() for i in  reg]
                    premio = Premio(reg[0], int(reg[1]), reg[2], reg[3])
                    db_filmes.insere_premio(premio)
                except:
                    print("\nERRO: Registro invalido, siga a formatacao correta: 'nome_evento', ano, 'tipo', 'nome_premio'\n")
                    continue 
                
            case "5": # filme
                print("Digite as informacoes do filme no formato: 'titulo_original', ano_producao, 'titulo_no_brasil', 'classe', 'idioma_original', arrecadacao_prim_ano")
                print("Exemplo: 'Wall-e', 2002, 'Wall-e', 'Animacao', 'Ingles', 500000")
                try:
                    reg = input()
                    reg = reg.split(",")
                    reg = [i.strip() for i in  reg]
                    filme = Filme(reg[0], int(reg[1]), reg[2], reg[3], reg[4], int(reg[5]))
                    db_filmes.insere_filme(filme)
                except:
                    print("\nERRO: Registro invalido, siga a formatacao correta: 'titulo_original', 'ano_producao', 'titulo_no_brasil', 'classe', 'idioma_original', 'arrecadacao_prim_ano'\n")
                    continue 
                
                flag = input('O filme é um documentário? S/N')
                
                if flag.upper() == 'S':
                    documentario = Documentario(reg[0], int(reg[1]))
                    db_filmes.insere_documentario(documentario)
                    
                else:
                    outro = Outros(reg[0], int(reg[1]))
                    db_filmes.insere_outros(outro)
                
            case "6": #indicacao
                print("Digite as informacoes da indicacao no formato: 'id_indicacao', 'nome_evento', ano, 'tipo', 'titulo_original', ano_producao, 'nome_artistico', 'foi_vencedor'")
                print("Exemplo: 0, 'Oscar', 2020, 'Melhor Ator', 'Jurassic Park', 1984, 'Adam Sandler', 'Não'")
                print(f'Lembre-se, é necessario já ter cadastrado os dados da edicao do evento, do filme e da pessoa"')
                try:
                    reg = input()
                    reg = reg.split(",")
                    reg = [i.strip() for i in  reg]
                    indicacao = Indicados(reg[0], reg[1], int(reg[2]), reg[3], reg[4], int(reg[5]), reg[6], reg[7])
                    db_filmes.insere_indicados(indicacao)
                except:
                    print("\nERRO: Registro invalido, siga a formatacao correta: 'id_indicacao', 'nome_evento', ano, 'tipo', 'titulo_original', ano_producao, 'nome_artistico', 'foi_vencedor'\n")
                    continue 
                
                print('Qual o papel dessa pessoa no filme?')
                print('Opções: diretor, produtor, roteirista, ator_principal, ator_elenco')
                flag = input('Papel no filme: ')
                print()
                
                match flag:
                    case 'diretor':
                        diretor = Diretores(reg[4], int(reg[5]), reg[6])
                        db_filmes.insere_diretores(diretor)
                        
                    case 'produtor':
                        produtor = Produtores(reg[4], int(reg[5]), reg[6])
                        db_filmes.insere_produtores(produtor)
                    
                    case 'roteirista':
                        roteirista = Roteiristas(reg[4], int(reg[5]), reg[6])
                        db_filmes.insere_roteiristas(roteirista)
                    
                    case 'ator_principal':
                        ator_princ = AtorPrincipal(reg[4], int(reg[5]), reg[6])
                        db_filmes.insere_ator_princ(ator_princ)
                    
                    case 'ator_elenco':
                        ator_elenco = AtorElenco(reg[4], int(reg[5]), reg[6])
                        db_filmes.insere_ator_elenco(ator_elenco)
                    case _:
                        print("\nERRO: Opcao invalida\n")
                        continue 
                    
            case "7": 
                return
            case "8":
                exit()
        
def grafico1(conn):
    consulta_sql = "SELECT * FROM tb_indicados WHERE foi_vencedor = 'Sim';"
    
    cursor = conn.cursor()

    cursor.execute(consulta_sql)

    resultados = cursor.fetchall()
    
    cursor.close()
    
    colunas = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(resultados, columns=colunas)
    
    sns.histplot(df['nome_artistico'])
    plt.show()
    
def grafico2(conn):
    consulta_sql = "SELECT * FROM tb_indicados WHERE foi_vencedor = 'Sim';"
    
    cursor = conn.cursor()

    cursor.execute(consulta_sql)

    resultados = cursor.fetchall()
    
    cursor.close()
    
    colunas = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(resultados, columns=colunas)
    
    sns.histplot(df['titulo_original'])
    plt.xticks(rotation=20, ha="right")
    plt.show()
    
def grafico3(conn):
    consulta_sql = "SELECT * FROM tb_filmes;"
    
    cursor = conn.cursor()

    cursor.execute(consulta_sql)

    resultados = cursor.fetchall()
    
    cursor.close()
    
    colunas = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(resultados, columns=colunas)
    
    plt.bar(df['titulo_original'], df['arrecadacao_prim_ano'])
    plt.xticks(rotation=30, ha="right")
    plt.show()
    
def lista_melhores_atores(conn):
    consulta_sql = "SELECT * FROM tb_indicados WHERE foi_vencedor = 'Sim' AND tipo = 'Melhor Ator';"
    
    cursor = conn.cursor()

    cursor.execute(consulta_sql)

    resultados = cursor.fetchall()
    
    cursor.close()
    
    colunas = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(resultados, columns=colunas)
    
    print()
    print('Lista de Melhores Atores')
    print(f" {df[['nome_evento','ano','nome_artistico']]}")
    print()
    
def indicados_do_premio(conn, premio):
    consulta_sql = f"SELECT * FROM tb_indicados WHERE nome_evento = {premio.nome_evento} AND ano = {premio.ano} AND tipo = {premio.tipo};"
    
    cursor = conn.cursor()

    cursor.execute(consulta_sql)

    resultados = cursor.fetchall()
    
    cursor.close()
    
    colunas = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(resultados, columns=colunas)
    
    print()
    print('Lista de indicados')
    print(f" {df[['nome_evento','ano','nome_artistico','titulo_original','foi_vencedor']]}")
    print()

def main():
    
    # ----- Alterar com as suas credenciais ------
    conn = pg.connect(
        database='filmes',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

    db_filmes = DataBase(conn)
    
    conn.autocommit = True
    
    menu_principal(db_filmes)
    
if __name__ == "__main__":
    main()
