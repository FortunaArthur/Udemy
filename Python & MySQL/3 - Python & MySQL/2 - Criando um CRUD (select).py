import MySQLdb

host = "localhost"
user = "Novinho"
password = "123456789"
db = "escolinha_de_cursinhos"
port = 3306
# Variavel pra receber o obejto de conexão
con = MySQLdb.connect(host,user,password,db,port)
# usar pra pegar resultado da conexão e também executar as consultas: c = con.cursor(), esse é o antes da mudança
c = con.cursor(MySQLdb.cursors.DictCursor)

#       Campos, Tabelas, Condição
def select(fields, tables, where=None):
# Definir como global pra ela ficar imutavel
    global c

# concatenar select com os campos e from com as tabelas
# ATENÇÃO, ESTA MERDA DE CONCATENAÇÃO TEMQ  TER A MERDA DOS ESPAÇOS SE NÃO DA ERRO E ELE NÃO ENTREGA Q É AKI, E SIM NO DQL, ENTÃO CUIDADO
    query = "SELECT " + fields + " FROM " + tables
# se tiver condição, se o where foi passado ele vem pro IF
    if (where):
        query = query + " WHERE " + where

    c.execute(query)
#fetchall() vai pegar tds os resultado do execute e retornar na função
    return c.fetchall()


print(select("*","alunos"))# imprimir a porra td
print("\n")
print(select("nome, cpf, estado","alunos"))# imprimir por campos
# se ficar assim printando vai ocupar mt linha
print("\n")
resultado = select("nome, cpf, estado", "alunos")
''''''''''''''''
#Mostrar tudo
print(resultado)
print("\n")

#Mostrar so o 1°
print(resultado[0])
print("\n")

#Mostrar só o campo
print(resultado[0][0])# nome
print(resultado[0][1])# cpf
print(resultado[0][2])# estado
print("\n")
'''''''''''''''''
# só assim fica feio, então vamo força o resultado das consultas serem dicionarios mudando o cursor, acrescentando dentro do cursor MySQLdb.cursors.DictCursor
# dps de ter feito isso, o resultado inves de me voltar uma tupla de tuplas, vai me voltar uma tupla de dicionario
print(resultado)
print("\n")

#Mostrar so o 1°
print(resultado[0])
print("\n")

#Mostrar so um campo do 1°
print(resultado[0]["nome"])
print(resultado[0]["cpf"])
print(resultado[0]["estado"])
# + intuitivo, sengundo o cara, acho q isso ai só ajuda a se perder menos, e na forma de mostrar ficar bunitin
