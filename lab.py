import sqlite3 as sql

conexao = sql.connect('dados.bd')
cursor= conexao.cursor()

#comando = 'CREATE TABLE livros (ISBN INTEGER PRIMARY KEY, TITULO VARCHAR(255), AUTOR VARCHAR(255), ano_de_publicação INTEGER, gênero VARCHAR (255) )'
#cursor.execute(comando)

def select():
    comando = 'SELECT * from livros'
    cursor.execute(comando)
    a=cursor.fetchall()
    print (a)

def insert():
    inserir = 'insert into livros values(?, ?, ?, ?, ?)'
    regitros = (4, "pizzas ", "andre", 2024,"" )
    cursor.execute(inserir, regitros)
    conexao.commit()

select()