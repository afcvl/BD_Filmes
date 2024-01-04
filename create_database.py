import psycopg2 as pg

def cria_database(conection, db_name):
    conn = conection

    conn.autocommit = True
    
    cursor = conn.cursor()
    
    sql = f''' create database {db_name}; '''
    
    cursor.execute(sql)

    conn.close()


conn = pg.connect(
    user='postgres',
    password='1234',
    host='localhost',
    port='5434'
)

cria_database(conn, 'filmes')

# Conectar ao banco de dados recém-criado (Filmes)
conn = pg.connect(
    database="filmes",
    user='postgres',
    password='1234',
    host='localhost',
    port='5434'
)
conn.autocommit = True

cursor = conn.cursor()

create_table_sql = '''

CREATE TABLE public.tb_Filme (
                Titulo_filme VARCHAR(50) NOT NULL,
                Ano DATE NOT NULL,
                TituloNoBrasil VARCHAR(50) NOT NULL,
                Classe VARCHAR(25) NOT NULL,
                IdiomaOrig VARCHAR(20) NOT NULL,
                ArrecPrimAno NUMERIC(12) NOT NULL,
                CONSTRAINT tb_filme_pk PRIMARY KEY (Titulo_filme)
);


CREATE TABLE public.tb_Outros (
                Titulo_filme VARCHAR(50) NOT NULL,
                CONSTRAINT tb_outros_pk PRIMARY KEY (Titulo_filme)
);


CREATE TABLE public.tb_Documentarios (
                Titulo_filme VARCHAR(50) NOT NULL,
                CONSTRAINT tb_documentarios_pk PRIMARY KEY (Titulo_filme)
);


CREATE TABLE public.tb_Estreia (
                Titulo_filme VARCHAR(50) NOT NULL,
                LocaisEstreia VARCHAR(25) NOT NULL,
                DataEstreia DATE NOT NULL,
                CONSTRAINT tb_estreia_pk PRIMARY KEY (Titulo_filme)
);


CREATE TABLE public.tb_Pessoa (
                NomeArt_pessoa VARCHAR(50) NOT NULL,
                Sexo VARCHAR(15) NOT NULL,
                AnoNasc DATE NOT NULL,
                Site VARCHAR(50) NOT NULL,
                AnoInicio DATE NOT NULL,
                Nome_verdadeiro VARCHAR(50) NOT NULL,
                Situacao VARCHAR(25) NOT NULL,
                Nro_total_anos NUMERIC,
                CONSTRAINT tb_pessoa_pk PRIMARY KEY (NomeArt_pessoa)
);


CREATE TABLE public.tb_AtorElenco (
                NomeArt_pessoa VARCHAR(50) NOT NULL,
                Titulo_filme VARCHAR(50) NOT NULL,
                CONSTRAINT tb_atorelenco_pk PRIMARY KEY (NomeArt_pessoa)
);


CREATE TABLE public.tb_AtorPrinc (
                NomeArt_pessoa VARCHAR(50) NOT NULL,
                Titulo_filme VARCHAR(50) NOT NULL,
                CONSTRAINT tb_atorprinc_pk PRIMARY KEY (NomeArt_pessoa)
);


CREATE TABLE public.tb_Produtor (
                NomeArt_pessoa VARCHAR(50) NOT NULL,
                Titulo_filme VARCHAR(50) NOT NULL,
                CONSTRAINT tb_produtor_pk PRIMARY KEY (NomeArt_pessoa)
);


CREATE TABLE public.tb_Roteirista (
                NomeArt_pessoa VARCHAR(50) NOT NULL,
                Titulo_filme VARCHAR(50) NOT NULL,
                CONSTRAINT tb_roteirista_pk PRIMARY KEY (NomeArt_pessoa)
);


CREATE TABLE public.tb_Diretor (
                NomeArt_pessoa VARCHAR(50) NOT NULL,
                Titulo_filme VARCHAR(50) NOT NULL,
                ePrincipal VARCHAR NOT NULL,
                CONSTRAINT tb_diretor_pk PRIMARY KEY (NomeArt_pessoa)
);


CREATE TABLE public.tb_EVENTOS (
                Nome_evento VARCHAR(30) NOT NULL,
                AnoInicio NUMERIC(4) NOT NULL,
                TIpo VARCHAR(20) NOT NULL,
                Nacionalidade VARCHAR(25) NOT NULL,
                CONSTRAINT tb_eventos_pk PRIMARY KEY (Nome_evento)
);


CREATE TABLE public.EDICAO (
                Ano NUMERIC(4) NOT NULL,
                Nome_evento_edicao VARCHAR(30) NOT NULL,
                Data DATE NOT NULL,
                Localizacao VARCHAR(25) NOT NULL,
                CONSTRAINT new_tableedicao PRIMARY KEY (Ano, Nome_evento_edicao)
);


CREATE TABLE public.tb_EJuri (
                Ano_ejuri NUMERIC(4) NOT NULL,
                Nome_evento VARCHAR(30) NOT NULL,
                NomeArt_ejuri VARCHAR(50) NOT NULL,
                CONSTRAINT tb_ejuri_pk PRIMARY KEY (Ano_ejuri, Nome_evento, NomeArt_ejuri)
);


CREATE TABLE public.Tb_PREMIO (
                Ano_premio NUMERIC(4) NOT NULL,
                Nome_evento_premio VARCHAR(30) NOT NULL,
                Tipo VARCHAR(20) NOT NULL,
                NomePremio VARCHAR(25) NOT NULL,
                CONSTRAINT tb_premio_pk PRIMARY KEY (Ano_premio, Nome_evento_premio, Tipo)
);


CREATE TABLE public.tb_eNominado (
                NomeArt_pessoa VARCHAR(50) NOT NULL,
                Ano_premio NUMERIC(4) NOT NULL,
                Nome_evento_premio VARCHAR(30) NOT NULL,
                Tipo VARCHAR(20) NOT NULL,
                Titulo_filme VARCHAR(50) NOT NULL,
                Ganhou BOOLEAN NOT NULL,
                CONSTRAINT tb_enominado_pk PRIMARY KEY (NomeArt_pessoa, Ano_premio, Nome_evento_premio, Tipo, Titulo_filme)
);


CREATE TABLE public.tb_FilmeNominado (
                Titulo_filme VARCHAR(50) NOT NULL,
                premiado VARCHAR(50) NOT NULL,
                Ano_premio NUMERIC(4) NOT NULL,
                Nome_evento_premio VARCHAR(30) NOT NULL,
                Tipo VARCHAR(20) NOT NULL,
                CONSTRAINT tb_filmenominado_pk PRIMARY KEY (Titulo_filme)
);


ALTER TABLE public.tb_Estreia ADD CONSTRAINT tb_filme_tb_estreia_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_Documentarios ADD CONSTRAINT tb_filme_tb_documentarios_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_Outros ADD CONSTRAINT tb_filme_tb_outros_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_FilmeNominado ADD CONSTRAINT tb_filme_tb_filmenominado_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_eNominado ADD CONSTRAINT tb_filme_tb_enominado_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_Diretor ADD CONSTRAINT tb_filme_tb_diretor_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_Produtor ADD CONSTRAINT tb_filme_tb_produtor_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_Roteirista ADD CONSTRAINT tb_filme_tb_roteirista_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_AtorElenco ADD CONSTRAINT tb_filme_tb_atorelenco_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_AtorPrinc ADD CONSTRAINT tb_filme_tb_atorprinc_fk
FOREIGN KEY (Titulo_filme)
REFERENCES public.tb_Filme (Titulo_filme)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_EJuri ADD CONSTRAINT tb_pessoa_tb_ejuri_fk
FOREIGN KEY (NomeArt_ejuri)
REFERENCES public.tb_Pessoa (NomeArt_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_Diretor ADD CONSTRAINT tb_pessoa_tb_diretor_fk
FOREIGN KEY (NomeArt_pessoa)
REFERENCES public.tb_Pessoa (NomeArt_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_Roteirista ADD CONSTRAINT tb_pessoa_tb_roteirista_fk
FOREIGN KEY (NomeArt_pessoa)
REFERENCES public.tb_Pessoa (NomeArt_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_Produtor ADD CONSTRAINT tb_pessoa_tb_produtor_fk
FOREIGN KEY (NomeArt_pessoa)
REFERENCES public.tb_Pessoa (NomeArt_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_AtorPrinc ADD CONSTRAINT tb_pessoa_tb_atorprinc_fk
FOREIGN KEY (NomeArt_pessoa)
REFERENCES public.tb_Pessoa (NomeArt_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_AtorElenco ADD CONSTRAINT tb_pessoa_tb_atorelenco_fk
FOREIGN KEY (NomeArt_pessoa)
REFERENCES public.tb_Pessoa (NomeArt_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_eNominado ADD CONSTRAINT tb_pessoa_tb_enominado_fk
FOREIGN KEY (NomeArt_pessoa)
REFERENCES public.tb_Pessoa (NomeArt_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.EDICAO ADD CONSTRAINT tb_eventos_edicao_fk
FOREIGN KEY (Nome_evento_edicao)
REFERENCES public.tb_EVENTOS (Nome_evento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Tb_PREMIO ADD CONSTRAINT edicao_tb_premio_fk
FOREIGN KEY (Ano_premio, Nome_evento_premio)
REFERENCES public.EDICAO (Ano, Nome_evento_edicao)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_EJuri ADD CONSTRAINT edicao_tb_ejuri_fk
FOREIGN KEY (Ano_ejuri, Nome_evento)
REFERENCES public.EDICAO (Ano, Nome_evento_edicao)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_FilmeNominado ADD CONSTRAINT tb_premio_tb_filmenominado_fk
FOREIGN KEY (Ano_premio, Nome_evento_premio, Tipo)
REFERENCES public.Tb_PREMIO (Ano_premio, Nome_evento_premio, Tipo)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.tb_eNominado ADD CONSTRAINT tb_premio_tb_enominado_fk
FOREIGN KEY (Ano_premio, Nome_evento_premio, Tipo)
REFERENCES public.Tb_PREMIO (Ano_premio, Nome_evento_premio, Tipo)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
'''

# Executar a query para criar a tabela
cursor.execute(create_table_sql)

# Fechar a conexão com o banco de dados 'Filmes'
conn.close()