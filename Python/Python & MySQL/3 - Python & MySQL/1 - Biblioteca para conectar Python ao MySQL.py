import MySQLdb

host = "localhost"
user = "Novinho"
password = "123456789"
db = "escolinha_de_cursinhos"
port = 3306
# Variavel pra receber o obejto de conexão
con = MySQLdb.connect(host,user,password,db,port)
