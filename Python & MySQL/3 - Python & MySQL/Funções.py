# Esse arquivo aki é pra num bagunçar dms os outros, pq kd arquivo ta cheio de comentarios
import MySQLdb

host = "localhost"
user = "Novinho"
password = "123456789"
db = "escolinha_de_cursinhos"
port = 3306

# Todas essas porra de funções foram confusas p krl, o mlku só explica pra ele, e tem muita gente perdida nessa merda MASSSS FODDASSE
con = MySQLdb.connect(host,user,password,db,port)
c = con.cursor(MySQLdb.cursors.DictCursor)
 
def select(fields,tables,where=None):
    global c
    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where
    c.execute(query)
    return c.fetchall()
 
def insert(values, table, fields=None):
    global c, con

    query = "INSERT INTO " + table

    if(fields):
        query = query + " (" + fields + ") "
    query = query + " VALUE " + ",".join(["( " + v + " )" for v in values])

    c.execute(query)
    con.commit()

def update(sets, table, where=None):
    global c, con

    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " ='" + value + "'" for field, value in sets.items()])
    
    if (where):
        query = query + "WHERE" + where

    c.execute(query)
    con.commit()

def delete(table, where):
    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()