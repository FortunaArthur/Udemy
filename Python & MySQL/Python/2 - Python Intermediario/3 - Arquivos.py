# Como to usando o vscode e ele da usn erros de procura de arquivo, coloca o (r"caminho todo do aruqivo"")
from venv import create


arquivo = open(r"C:\Users\arthu\Documents\Repositórios GitHub\Udemy\Python & MySQL\Python\2 - Python Intermediario\arquivo1.txt")
print(arquivo)# retorna infos sobre o arquivo e não do aruqivo (arquivo1.txt' mode='r' encoding='cp1252')

# Ler as Linhas
linhas = arquivo.readlines()# ele vai pegar cada linha e vai jogar dentro de uma lista
# AVISO, tem a readline(QUE VAI LER 1 LINHA SÓ) e a readlines(QUE LE TODAS), função no plural e no singular
print(linhas)
# printar linha por linha
for linha in linhas:
    print(linha)

# Ler o Conteudo do arquivo
texto_completo = arquivo.read()
print(texto_completo)

# Criar um Novo Arquivo
criar_arquivo = open("arquivo2.txt","w")# se vc usar create ele vai criar uma pasta 
# o comando criou fora da pasta que eu queria, então vamo criar no lugar certo
criar_certo = open(r"C:\Users\arthu\Documents\Repositórios GitHub\Udemy\Python & MySQL\Python\2 - Python Intermediario\arquivo2.text", "w")

# Escrever no Arquivo
criar_certo.write("Esse é o 2° Arquivo criado para essa aula")
# Se vc olhar agr vai ver que os acentos caracteres especiais ficaram com sinal de ?
# Pra resolver é só usar open("arquivo.txt", encoding="utf-8")
criar_certo = open(r"C:\Users\arthu\Documents\Repositórios GitHub\Udemy\Python & MySQL\Python\2 - Python Intermediario\arquivo2.text", "w", encoding="utf-8")
# o w no final quer dizer q ele vai criar 1 novo arquivo e caso ele ja exista ele paga e cria outro novo
criar_certo.write("Esse é o 2° Arquivo criado para essa aula")
# agr ta certin

# Fechar Arquivo
criar_certo.close()

# E SE.........
# vc usar o metodo w no arquivo1?
escrever = open(r"C:\Users\arthu\Documents\Repositórios GitHub\Udemy\Python & MySQL\Python\2 - Python Intermediario\arquivo1.txt", "w", encoding="utf-8")
''''''''''''''''
# É isso que está no arquivo 1 agr
SALVE GUYS
ISSO AKI É UM ARQUIVO TXT
PARA A PARTE DE ARQUIVOS
'''''''''''''''''
escrever.write("EU VO MUDA A PORRA TODA \n")
# ele vai apagar e escrever por cima
escrever.close()
