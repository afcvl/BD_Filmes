from entidades import * 
from insercoes import *

def menu_principal(db_filmes):
    
    while True:
        print("1. Cadastrar registros")
        print("2. Gerar grafico com os 10 autores com maior numero de premios")
        print("3. Gerar grafico com os 10 filmes mais premiados")
        print("4. Gerar grafico com os 10 filmes de maior arrecadacao")
        print("5. Dado um premio, pesquisar quais autores ou filmes foram nominados e premiados")
        print("6. Sair")
        opcao = input("Digite a sua opcao: ")
        match opcao:
            case "1":
                menu_cadastro(db_filmes)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                exit()

def menu_cadastro(db_filmes):
    while True:
        print("O que voce deseja cadastrar?")
        print("1. Pessoas")
        print("2. Eventos")
        print("3. Edicao de evento")
        print("4. Premios")
        print("5. Filmes")        
        print("6. Indicações")

        print("7. Menu principal")
        print("8. Sair")
        opcao = input("Digite a sua opcao: ")
        match opcao:
            case "1":
                print("Digite as informacoes da pessoa no formato: 'nome_artistico', 'nome_real', 'sexo', ano_nascimento, 'site', ano_inicio, total_anos, 'situacao'") 
                print("Exemplo: ('Johnny Depp', 'John Christopher Depp II', 'Masculino', 1963, 'WWW.jdepp.com', 1984, 38, 'Vivo')"),
                reg = input()
                reg = reg.split(",")
                reg = [i.strip() for i in  reg]
                pessoa = Pessoa(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7])
                db_filmes.insere_pessoa(pessoa)
                
                
            case "2":
                print("Digite as informacoes do evento no formato: 'nome_evento','tipo', 'nacionalidade', ano_inicio")
                print("Exemplo: 'Oscar', 'Premiacao', 'Americano', 1929")
                reg = input()
                reg = reg.split(",")
                reg = [i.strip() for i in  reg]
                evento = Eventos(reg[0], reg[1], reg[2], reg[3])
                db_filmes.insere_evento(evento)
                print()
                flag = input('deseja inserir uma edição do evento? S/N: ')
                print()
                if flag == 'S':
                    print("Digite as informacoes da edicao no formato: 'localizacao','data_realizacao', 'nome_evento', ano")
                    print("Exemplo: 'Nova York', '05-05-2020', 'Oscar', 2020")
                    print(f"Lembre-se que o evento deve ser '{reg[0]}'")
                    reg = input()
                    reg = reg.split(",")
                    reg = [i.strip() for i in  reg]
                    edicao = Edicao(reg[0], reg[1], reg[2], reg[3])
                    db_filmes.insere_edicao(edicao)
                    
            
            case "3":
                print("Digite as informacoes da edicao no formato: 'localizacao','data_realizacao', 'nome_evento', ano")
                print("Exemplo: 'Nova York', '05-05-2020', 'Oscar', 2020")
                print(f'Lembre-se de utilizar o nome de um evento existente"')
                reg = input()
                reg = reg.split(",")
                reg = [i.strip() for i in  reg]
                edicao = Edicao(reg[0], reg[1], reg[2], reg[3])
                db_filmes.insere_edicao(edicao)
                
    
            case "4":
                print("Digite as informacoes do premio no formato: 'nome_evento', ano, 'tipo', 'nome_premio'")
                print("Exemplo: 'Oscar', 2020, 'Melhor Ator', 'Oscar'")
                reg = input()
                reg = reg.split(",")
                reg = [i.strip() for i in  reg]
                premio = Premio(reg[0], reg[1], reg[2], reg[3])
                db_filmes.insere_premio(premio)
                
            case "5":
                print("Digite as informacoes do filme no formato: 'titulo_original', ano_producao, 'titulo_no_brasil', 'classe', 'idioma_original', arrecadacao_prim_ano")
                print("Exemplo: 'Wall-e', 2002, 'Wall-e', 'Animacao', 'Ingles', 500000")
                reg = input()
                reg = reg.split(",")
                reg = [i.strip() for i in  reg]
                filme = Filme(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
                db_filmes.insere_filme(filme)
                
                flag = input('O filme é um documentário? s/n')
                
                if flag.lower() == 's':
                    documentario = Documentario(reg[0], reg[1])
                    db_filmes.insere_documentario(documentario)
                    
                else:
                    outro = Outros(reg[0], reg[1])
                    db_filmes.insere_outros(outro)
                
    
            case "6":
                print("Digite as informacoes da indicacao no formato: 'id_indicacao', 'nome_evento', ano, 'tipo', 'titulo_original', 'ano_producao', 'nome_artistico', 'foi_vencedor'")
                print("Exemplo: 0, 'Oscar', 2020, 'Melhor Ator', 'Jurassic Park', 1984, 'Adam Sandler', 'Não'")
                print(f'Lembre-se, é necessario já ter cadastrado os dados do evento, da edicao, do filme e da pessoa"')
                reg = input()
                reg = reg.split(",")
                reg = [i.strip() for i in  reg]
                indicacao = Indicados(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7])
                db_filmes.insere_indicados(indicacao)
                
                print()
                print('Qual o papel dessa pessoa no filme?')
                print('Opções: diretor, produtor, roteirista, ator_principal, ator_elenco')
                flag = input('Papel no filme: ')
                print()
                
                match flag:
                    case 'diretor':
                        diretor = Diretores(reg[4], reg[5], reg[6])
                        db_filmes.insere_diretores(diretor)
                        
                    case 'produtor':
                        produtor = Produtores(reg[4], reg[5], reg[6])
                        db_filmes.insere_produtores(produtor)
                    
                    case 'roteirista':
                        roteirista = Roteiristas(reg[4], reg[5], reg[6])
                        db_filmes.insere_roteiristas(roteirista)
                    
                    case 'ator_principal':
                        ator_princ = AtorPrincipal(reg[4], reg[5], reg[6])
                        db_filmes.insere_ator_princ(ator_princ)
                    
                    case 'ator_elenco':
                        ator_elenco = AtorElenco(reg[4], reg[5], reg[6])
                        db_filmes.insere_ator_elenco(ator_elenco)
                    

            case "7": 
                return
            case "8":
                exit()
            
def main():
    
    conn = pg.connect(
        database='filmes',
        user='postgres',
        password='1234',
        host='localhost',
        port='5434'
    )

    db_filmes = DataBase(conn)
    
    conn.autocommit = True
    
    menu_principal(db_filmes)
    

if __name__ == "__main__":
    main()