import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
email_generico = "sem_email@gmail.com"

def criar_tabela(cursor):
    cursor.execute("""CREATE TABLE clientes 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(100), email VARCHAR(150))""")

def inserir_registro(cursor=cursor,conexao=conexao,nome=None,email=email_generico):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome,email) VALUES (?,?)',data)
    conexao.commit()

# inserir_registro(nome="gio",email="gio@gmail.com")

def atualizar_regstro(nome,email,id,cursor=cursor,conexao=conexao):
    data = (nome,email,id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;',data)
    conexao.commit()


def deletando_regstro(id,cursor=cursor,conexao=conexao):
    data = (id)
    cursor.execute('DELETE FROM clientes WHERE id=?;',(data,))
    conexao.commit()

def inserir_massivo(dados,cursor=cursor,conexao=conexao):
    data = (dados)
    cursor.executemany('INSERT INTO clientes (nome,email) VALUES (?,?)',data)
    conexao.commit()

lista = []

# while True:

#     dados1 = input("Digite seu nome:")
#     dados2 = input("Digite seu e-mail:")
#     valores = (dados1,dados2)
#     lista.append(valores)

#     cont = input("Quer continuar ? [S/N]").upper()
#     if cont == "N":
#         break

cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?)", ('Teste 3', 'Teste3@gmail.com'))
cursor.execute("INSERT INTO clientes (id,nome,email) VALUES (?,?,?)", (9,'Teste 4', 'Teste4@gmail.com'))

conexao.commit()
