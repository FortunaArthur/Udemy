from Funções import select
import MySQLdb

host = "localhost"
user = "Novinho"
password = "123456789"
db = "escolinha_de_cursinhos"
port = 3306

con = MySQLdb.connect(host,user,password,db,port)
c = con.cursor(MySQLdb.cursors.DictCursor)

def update(sets, table, where=None):
    global c, con

    query = "UPDATE " + table# to entendeno mais nd, + o cara só segue a linha dele e ta mais preocupado com qtd de linhas do q com didatica etão fds
    query = query + " SET " + ",".join([field + " ='" + value + "'" for field, value in sets.items()])
    
    if (where):
        query = query + "WHERE" + where

    c.execute(query)
    con.commit()

update({"nome":"Joao Martins","cidade": "Curitiba"}, "alunos")

print(select("*", "alunos", "id_aluno = 1"))