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
        print("2. Eventos e Premios")
        print("3. Nominações")
        print("4. Premiações e Filmes")
        print("5. Menu principal")
        print("6. Sair")
        opcao = input("Digite a sua opcao: ")
        match opcao:
            case "1":
                # to-do
                print("Digite as informacoes da pessoa (formato: nome_art_pessoa, sexo, ano_nasc, site, ano_inicio, nome_verdadeiro, situacao, nro_total_anos)") 
                print("Exemplo: Brad Pitt, , 1963, , William Bradley Pitt, Ativo, ")
                reg = input()
                reg = reg.split(",")
                pessoa = Pessoa(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7])
                db_filmes.insere_pessoa(pessoa)
                papel = input("Papel da pessoa (formato: AtorElenco, AtorPrinc, Produtor, Roteirista, Diretor): ")

            case "2":
                print("Digite as informacoes do evento (formato: nome_evento, ano_inicio, tipo, nacionalidade)")
                reg = input()
                reg = reg.split(",")
                evento = Eventos(reg[0], reg[1], reg[2], reg[3])
                db_filmes.insere_evento(evento)
                quantidade_premios = int(input("Quantos premios deseja inserir: "))
                print("Digite as informacoes do(s) premio(s) (formato: ano_premio, nome_evento_premio, tipo, nome_premio)")
                for i in range(len(quantidade_premios)):
                    reg = input()
                    reg = reg.split(",")
                    premio = Premio(reg[0], reg[1], reg[2], reg[3])
                    db_filmes.insere_premio(premio)

            case "3":
                # to-do
                tipo = input("Deseja inserir uma nominacao de filme(1) ou pessoa(2): ")
                match tipo:
                    case "1":
                        print("Digite as informacoes da nonimacao do filme (formato: titulo_filme, premiado, ano_premio, nome_evento_premio, tipo)")
                        reg = input()
                        reg = reg.split(",")
                        nominacao_filme = FilmeNominado(reg[0], reg[1], reg[2], reg[3], reg[4])
                        db_filmes.insere_nomiacao()

                    case "2":
                        print("Digite as informacoes da nominacao da pessoa (formato: nome_art_pessoa, ano_premio, nome_evento_premio, tipo, titulo_filme, ganhou)")
                        reg = input()
                        reg = reg.split(",")
                        nominacao_pessoa = ENominado(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
                        db_filmes.insere_nominacao()
            case "4":
                pass
            case "5":
                return # Volta ao menu principal
            case "6":
                exit()


def main():
    db_filmes = Database() # to-do
    menu_principal(db_filmes)
    

if __name__ == "__main__":
    main()
