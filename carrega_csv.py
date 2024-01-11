# def carrega_evento_csv(self, arquivo):
#     registros = arquivo.read()
#     registros = registros.linesplit()
    
#     for reg in registros:
#         reg = reg.split(",")
#         evento = Eventos(reg[0], reg[1], reg[2], reg[3])
#         self.insere_evento(evento)

# def carrega_pessoa_csv(self, arquivo):
#     registros = arquivo.read()
#     registros = registros.linesplit()
    
#     for reg in registros:
#         reg = reg.split(",")
#         pessoa = Pessoa(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7])
#         self.insere_pessoa(pessoa)

# def carrega_premio_csv(self, arquivo):
#     registros = arquivo.read()
#     registros = registros.linesplit()
    
#     for reg in registros:
#         reg = reg.split(",")
#         premio = Premio(reg[0], reg[1], reg[3], reg[4])
#         self.insere_premio(premio)

# def carrega_nomiacao_csv(self, arquivo):
#     registros = arquivo.read()
#     registros = registros.linesplit()
    
#     for reg in registros:
#         reg = reg.split(",")
#         nomiacao = ENominado(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
#         self.insere_nomiacao(nomiacao)

# def carrega_filme_csv(self, arquivo):
#     registros = arquivo.read()
#     registros = registros.linesplit()
    
#     for reg in registros:
#         reg = reg.split(",")
#         filme = Filme(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
#         self.insere_filme(filme)