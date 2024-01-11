drop_table_sql = '''

drop table tb_jurados;

drop table tb_indicados;

drop table tb_premio;

drop table tb_edicao;

drop table tb_eventos;

drop table tb_documentarios;

drop table tb_locais_estreia;

drop table tb_diretores;

drop table tb_produtores;

drop table tb_roteiristas;

drop table tb_ator_principal;

drop table tb_ator_elenco;

drop table tb_outros;

drop table tb_pessoa;

drop table tb_filmes;
'''

create_table_sql = '''

CREATE TABLE tb_eventos (
	nome_evento VARCHAR(50) NOT NULL,
	tipo VARCHAR(50),
	nacionalidade VARCHAR(50),
	ano_inicio NUMERIC(4),
	PRIMARY KEY (nome_evento)
);

CREATE TABLE tb_edicao (
	localizacao VARCHAR(50),
	data_realizacao DATE,
	nome_evento VARCHAR(50),
	ano NUMERIC(4),
	FOREIGN KEY (nome_evento) REFERENCES tb_eventos(nome_evento),
	PRIMARY KEY (nome_evento, ano)

);

CREATE TABLE tb_premio (
	nome_evento VARCHAR(50),
	ano NUMERIC(4),
	tipo VARCHAR(50),
	nome_premio VARCHAR(50),
	FOREIGN KEY (nome_evento, ano) REFERENCES tb_edicao(nome_evento, ano) ON DELETE CASCADE,
	PRIMARY KEY (nome_evento, ano, tipo)
);

CREATE TABLE tb_pessoa (
	nome_artistico VARCHAR(50),
	nome_real VARCHAR(50),
	sexo VARCHAR(20),
	ano_nascimento NUMERIC(4),
	site VARCHAR(50),
	ano_inicio NUMERIC(4),
	total_anos NUMERIC,
	situacao VARCHAR(50),
	PRIMARY KEY (nome_artistico)
);

CREATE TABLE tb_jurados (
	id_jurado NUMERIC,
	Nome_evento VARCHAR(50),
	Ano NUMERIC(4),
	Tipo VARCHAR(50),
	nome_artistico VARCHAR(50),
	PRIMARY KEY (id_jurado),
	FOREIGN KEY (nome_evento, ano, tipo) REFERENCES tb_premio(nome_evento, ano, tipo) ON DELETE CASCADE,
	FOREIGN KEY (nome_artistico) REFERENCES tb_pessoa(nome_artistico) ON DELETE CASCADE
);

CREATE TABLE tb_filmes (
	titulo_original VARCHAR(50),
	ano_producao NUMERIC(4),
	titulo_no_brasil VARCHAR(50),
	classe VARCHAR(50),
	idioma_original VARCHAR(50),
	arrecadacao_prim_ano NUMERIC,
	PRIMARY KEY (titulo_original, ano_producao)
);

CREATE TABLE tb_documentarios (
	titulo_original VARCHAR(50),
	ano_producao NUMERIC(4),
	PRIMARY KEY (titulo_original, ano_producao),
	FOREIGN KEY (titulo_original, ano_producao) REFERENCES tb_filmes(titulo_original, ano_producao)	
	ON DELETE CASCADE
);

CREATE TABLE tb_outros (
	titulo_original VARCHAR(50),
	ano_producao NUMERIC(4),
	PRIMARY KEY (titulo_original, ano_producao),
	FOREIGN KEY (titulo_original, ano_producao) REFERENCES tb_filmes(titulo_original, ano_producao)	
	ON DELETE CASCADE
);

CREATE TABLE tb_locais_estreia (
	id_estreia NUMERIC,
	titulo_original VARCHAR(50),
	ano_producao NUMERIC(4),
	PRIMARY KEY (id_estreia),
	FOREIGN KEY (titulo_original, ano_producao) REFERENCES tb_filmes(titulo_original, ano_producao)	
	ON DELETE CASCADE
);

CREATE TABLE tb_indicados (
	id_indicacao NUMERIC(7),
	nome_evento VARCHAR(50),
	ano NUMERIC(4),
	tipo VARCHAR(50),
	titulo_original VARCHAR(50),
	ano_producao NUMERIC(4),
	nome_artistico VARCHAR(50),
	foi_vencedor VARCHAR(3),
	PRIMARY KEY (id_indicacao),
	FOREIGN KEY (nome_evento, ano, tipo) REFERENCES tb_premio(nome_evento, ano, tipo) ON DELETE CASCADE,
	FOREIGN KEY (titulo_original, ano_producao) REFERENCES tb_filmes(titulo_original, ano_producao) ON DELETE CASCADE,
	FOREIGN KEY (nome_artistico) REFERENCES tb_pessoa(nome_artistico) ON DELETE CASCADE
);

CREATE TABLE tb_diretores (
	titulo_filme VARCHAR(50),
	ano_producao NUMERIC(4),
	nome_artistico VARCHAR(50),
	PRIMARY KEY (titulo_filme, ano_producao, nome_artistico),
	FOREIGN KEY (titulo_filme, ano_producao) REFERENCES tb_filmes(titulo_original, ano_producao) ON DELETE CASCADE,
	FOREIGN KEY (nome_artistico) REFERENCES tb_pessoa(nome_artistico) ON DELETE CASCADE
);

CREATE TABLE tb_produtores (
	titulo_filme VARCHAR(50),
	ano_producao NUMERIC(4),
	nome_artistico VARCHAR(50),
	PRIMARY KEY (titulo_filme, ano_producao, nome_artistico),
	FOREIGN KEY (titulo_filme, ano_producao) REFERENCES tb_filmes(titulo_original, ano_producao) ON DELETE CASCADE,
	FOREIGN KEY (nome_artistico) REFERENCES tb_pessoa(nome_artistico) ON DELETE CASCADE
);

CREATE TABLE tb_roteiristas (
	titulo_filme VARCHAR(50),
	ano_producao NUMERIC(4),
	nome_artistico VARCHAR(50),
	PRIMARY KEY (titulo_filme, ano_producao, nome_artistico),
	FOREIGN KEY (titulo_filme, ano_producao) REFERENCES tb_filmes(titulo_original, ano_producao) ON DELETE CASCADE,
	FOREIGN KEY (nome_artistico) REFERENCES tb_pessoa(nome_artistico) ON DELETE CASCADE
);

CREATE TABLE tb_ator_principal (
	titulo_filme VARCHAR(50),
	ano_producao NUMERIC(4),
	nome_artistico VARCHAR(50),
	PRIMARY KEY (titulo_filme, ano_producao, nome_artistico),
	FOREIGN KEY (titulo_filme, ano_producao) REFERENCES tb_outros(titulo_original, ano_producao) ON DELETE CASCADE,
	FOREIGN KEY (nome_artistico) REFERENCES tb_pessoa(nome_artistico) ON DELETE CASCADE
);

CREATE TABLE tb_ator_elenco (
	titulo_filme VARCHAR(50),
	ano_producao NUMERIC(4),
	nome_artistico VARCHAR(50),
	PRIMARY KEY (titulo_filme, ano_producao, nome_artistico),
	FOREIGN KEY (titulo_filme, ano_producao) REFERENCES tb_outros(titulo_original, ano_producao) ON DELETE CASCADE,
	FOREIGN KEY (nome_artistico) REFERENCES tb_pessoa(nome_artistico) ON DELETE CASCADE
);
'''