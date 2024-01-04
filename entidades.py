class Filme:
    def __init__(self, titulo_filme, ano, titulo_brasil, classe, idioma_orig, arrec_prim_ano):
        self.titulo_filme = titulo_filme
        self.ano = ano
        self.titulo_brasil = titulo_brasil
        self.classe = classe
        self.idioma_orig = idioma_orig
        self.arrec_prim_ano = arrec_prim_ano

class Outros:
    def __init__(self, titulo_filme):
        self.titulo_filme = titulo_filme

class Documentarios:
    def __init__(self, titulo_filme):
        self.titulo_filme = titulo_filme

class Estreia:
    def __init__(self, titulo_filme, locais_estreia, data_estreia):
        self.titulo_filme = titulo_filme
        self.locais_estreia = locais_estreia
        self.data_estreia = data_estreia

class Pessoa:
    def __init__(self, nome_art_pessoa, sexo, ano_nasc, site, ano_inicio, nome_verdadeiro, situacao, nro_total_anos):
        self.nome_art_pessoa = nome_art_pessoa
        self.sexo = sexo
        self.ano_nasc = ano_nasc
        self.site = site
        self.ano_inicio = ano_inicio
        self.nome_verdadeiro = nome_verdadeiro
        self.situacao = situacao
        self.nro_total_anos = nro_total_anos

class AtorElenco:
    def __init__(self, nome_art_pessoa, titulo_filme):
        self.nome_art_pessoa = nome_art_pessoa
        self.titulo_filme = titulo_filme

class AtorPrinc:
    def __init__(self, nome_art_pessoa, titulo_filme):
        self.nome_art_pessoa = nome_art_pessoa
        self.titulo_filme = titulo_filme

class Produtor:
    def __init__(self, nome_art_pessoa, titulo_filme):
        self.nome_art_pessoa = nome_art_pessoa
        self.titulo_filme = titulo_filme

class Roteirista:
    def __init__(self, nome_art_pessoa, titulo_filme):
        self.nome_art_pessoa = nome_art_pessoa
        self.titulo_filme = titulo_filme

class Diretor:
    def __init__(self, nome_art_pessoa, titulo_filme, e_principal):
        self.nome_art_pessoa = nome_art_pessoa
        self.titulo_filme = titulo_filme
        self.e_principal = e_principal

class Eventos:
    def __init__(self, nome_evento, ano_inicio, tipo, nacionalidade):
        self.nome_evento = nome_evento
        self.ano_inicio = ano_inicio
        self.tipo = tipo
        self.nacionalidade = nacionalidade

class Edicao:
    def __init__(self, ano, nome_evento_edicao, data, localizacao):
        self.ano = ano
        self.nome_evento_edicao = nome_evento_edicao
        self.data = data
        self.localizacao = localizacao

class EJuri:
    def __init__(self, ano_ejuri, nome_evento, nome_art_ejuri):
        self.ano_ejuri = ano_ejuri
        self.nome_evento = nome_evento
        self.nome_art_ejuri = nome_art_ejuri

class Premio:
    def __init__(self, ano_premio, nome_evento_premio, tipo, nome_premio):
        self.ano_premio = ano_premio
        self.nome_evento_premio = nome_evento_premio
        self.tipo = tipo
        self.nome_premio = nome_premio

class ENominado:
    def __init__(self, nome_art_pessoa, ano_premio, nome_evento_premio, tipo, titulo_filme, ganhou):
        self.nome_art_pessoa = nome_art_pessoa
        self.ano_premio = ano_premio
        self.nome_evento_premio = nome_evento_premio
        self.tipo = tipo
        self.titulo_filme = titulo_filme
        self.ganhou = ganhou

class FilmeNominado:
    def __init__(self, titulo_filme, premiado, ano_premio, nome_evento_premio, tipo):
        self.titulo_filme = titulo_filme
        self.premiado = premiado
        self.ano_premio = ano_premio
        self.nome_evento_premio = nome_evento_premio
        self.tipo = tipo
