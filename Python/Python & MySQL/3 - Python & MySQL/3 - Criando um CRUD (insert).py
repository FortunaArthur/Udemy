from Funções import select

import MySQLdb

host = "localhost"
user = "Novinho"
password = "123456789"
db = "escolinha_de_cursinhos"
port = 3306

con = MySQLdb.connect(host,user,password,db,port)
c = con.cursor(MySQLdb.cursors.DictCursor)

#           Valores, Tabela, Campo
def insert(values, table, fields=None):
    # ja q estamos fazendo 1 insert é nescessario o con para conexão
    global c, con

    query = "INSERT INTO " + table
                      # Fields
# INSERT INTO <tabela> (campos) VALUES (), (), ().........

    if(fields):
        query = query + " (" + fields + ") "
# concatenar os values com a virgula, e nela será feita 1 join, já que os parenteses são separados por virgulas
    query = query + " VALUE " + ",".join(["( " + v + " )" for v in values])# concatenar o V com parenteses

    c.execute(query)
    con.commit()

values = [
"default, 'João Pereira', '2000-01-01', 'Rua Carlos, 123', 'Betim', 'MG', '12345678912'"]
# Mano passei mt raiva nesse codigo, num vocomenta N, o cara ta explicando mal pkrl, vamo de next
insert(values, "alunos")

print(select("*", "alunos"))
