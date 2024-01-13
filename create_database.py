import psycopg2 as pg

def cria_database(conection, db_name):
    conn = conection

    conn.autocommit = True
    
    cursor = conn.cursor()
    
    sql = f''' create database {db_name}; '''
    
    cursor.execute(sql)

    conn.close()

# ----- Alterar com as suas credenciais ------
conn = pg.connect(
    user='postgres',
    password='1234',
    host='localhost',
    port='5432'
)

cria_database(conn, 'filmes')

# Conectar ao banco de dados recém-criado (Filmes)
# ----- Alterar com as suas credenciais ------
conn = pg.connect(
    database="filmes",
    user='postgres',
    password='1234',
    host='localhost',
    port='5432'
)
conn.autocommit = True

cursor = conn.cursor()

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
	FOREIGN KEY (nome_evento) REFERENCES tb_eventos(nome_evento) ON DELETE CASCADE,
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
	local VARCHAR(50),
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

# Executar a query para criar a tabela
cursor.execute(create_table_sql)

# Fechar a conexão com o banco de dados 'Filmes'
conn.close()