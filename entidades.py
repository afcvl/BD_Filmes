class Eventos:
    def __init__(self, nome_evento, tipo, nacionalidade, ano_inicio):
        self.nome_evento = nome_evento
        self.tipo = tipo
        self.nacionalidade = nacionalidade
        self.ano_inicio = ano_inicio
        
class Edicao:
    def __init__(self, localizacao, data_realizacao, nome_evento, ano):
        self.localizacao = localizacao
        self.data_realizacao = data_realizacao
        self.nome_evento = nome_evento
        self.ano = ano

class Premio:
    def __init__(self, nome_evento, ano, tipo, nome_premio):
        self.nome_evento = nome_evento
        self.ano = ano
        self.tipo = tipo
        self.nome_premio = nome_premio

class Pessoa:
    def __init__(self, nome_artistico, nome_real, sexo, ano_nascimento, site, ano_inicio, total_anos, situacao):
        self.nome_artistico = nome_artistico
        self.nome_real = nome_real
        self.sexo = sexo
        self.ano_nascimento = ano_nascimento
        self.site = site
        self.ano_inicio = ano_inicio
        self.total_anos = total_anos
        self.situacao = situacao

class Jurados:
    def __init__(self, id_jurado, nome_evento, ano, tipo, nome_artistico):
        self.id_jurado = id_jurado
        self.nome_evento = nome_evento
        self.ano = ano
        self.tipo = tipo
        self.nome_artistico = nome_artistico       
        
class Filme:
    def __init__(self, titulo_original, ano_producao, titulo_no_brasil, classe, idioma_original, arrecadacao_prim_ano):
        self.titulo_original = titulo_original
        self.ano_producao = ano_producao
        self.titulo_no_brasil = titulo_no_brasil
        self.classe = classe
        self.idioma_original = idioma_original
        self.arrecadacao_prim_ano = arrecadacao_prim_ano
        
class Documentario:
    def __init__(self, titulo_original, ano_producao):
        self.titulo_original = titulo_original
        self.ano_producao = ano_producao

class Outros:
    def __init__(self, titulo_original, ano_producao):
        self.titulo_original = titulo_original
        self.ano_producao = ano_producao

class LocaisEstreia:
    def __init__(self, id_estreia, titulo_original, ano_producao, local):
        self.id_estreia = id_estreia
        self.titulo_original = titulo_original
        self.ano_producao = ano_producao
        self.local = local

class Indicados:
    def __init__(self, id_indicacao, nome_evento, ano, tipo, titulo_original, ano_producao, nome_artistico, foi_vencedor):
        self.id_indicacao = id_indicacao
        self.nome_evento = nome_evento
        self.ano = ano
        self.tipo = tipo
        self.titulo_original = titulo_original
        self.ano_producao = ano_producao
        self.nome_artistico = nome_artistico
        self.foi_vencedor = foi_vencedor

class Diretores:
    def __init__(self, titulo_filme, ano_producao, nome_artistico):
        self.titulo_filme = titulo_filme
        self.ano_producao = ano_producao
        self.nome_artistico = nome_artistico

class Produtores:
    def __init__(self, titulo_filme, ano_producao, nome_artistico):
        self.titulo_filme = titulo_filme
        self.ano_producao = ano_producao
        self.nome_artistico = nome_artistico

class Roteiristas:
    def __init__(self, titulo_filme, ano_producao, nome_artistico):
        self.titulo_filme = titulo_filme
        self.ano_producao = ano_producao
        self.nome_artistico = nome_artistico

class AtorPrincipal:
    def __init__(self, titulo_filme, ano_producao, nome_artistico):
        self.titulo_filme = titulo_filme
        self.ano_producao = ano_producao
        self.nome_artistico = nome_artistico

class AtorElenco:
    def __init__(self, titulo_filme, ano_producao, nome_artistico):
        self.titulo_filme = titulo_filme
        self.ano_producao = ano_producao
        self.nome_artistico = nome_artistico