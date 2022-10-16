from Funções import select
import MySQLdb

host = "localhost"
user = "Novinho"
password = "123456789"
db = "escolinha_de_cursinhos"
port = 3306

con = MySQLdb.connect(host,user,password,db,port)
c = con.cursor(MySQLdb.cursors.DictCursor)

def delete(table, where):
    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()

# Essa ai é a merda do codigo dele, da erro por causa das chaves extrangeiras e o maldito nem se preocupo em fazer uma aual pra explicar como faz pra resolver pelo python
# então FODA-SE

 

