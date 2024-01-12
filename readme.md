# EP 3 Banco de dados I

## Dependências

Primeiramente é necessário instalar o Pip, um gerenciador de pacotes para Python

Ubuntu, Linux Mint, Debian:

```
sudo apt install python3-pip
```

Arch-based:

```
sudo pacman -S python-pip
```

# Instalação automática

Para simplificar a instalação das dependências utilizadas no sistema, execute o script de instalação usando o seguinte comando (apenas para sistemas Linux)

```
./dependecy.sh 
```

# Instalação manual

- Psycopg2

```
pip install psycopg2 
```

[Documentação de instalação do Psycopg2](https://www.psycopg.org/docs/install.html#quick-install)

- SQLAlchemy

```
pip install SQLAlchemy 
```

[Documentação de instalação do SQLAlchemy](https://docs.sqlalchemy.org/en/20/intro.html#installation)

- Seaborn

```
pip install seaborn 
```

[Documentação de instalação do Seaborn](https://seaborn.pydata.org/installing.html)

- Pandas

```
pip install pandas
```

[Documentação de instalação do Pandas](https://pandas.pydata.org/docs/getting_started/install.html)

- Matplotlib

```
pip install matplotlib 
```

[Documentação de instalação do Matplotlib](https://matplotlib.org/stable/users/installing/index.html)

## Instruções de Uso:

- Passo 1. É necessário criar um server local no Pgadmin4 antes de iniciar a execução da aplicação

- Passo 2. Alterar função pg.connect com as informações do server local no arquivo create_database.py para funcionar no banco local 

- Passo 3. Rodar o script create_database.py apenas uma vez

- Passo 4. Utilizar o sistema em __main__.py
