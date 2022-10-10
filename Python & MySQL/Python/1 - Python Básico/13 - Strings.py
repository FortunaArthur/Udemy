# Strings é umtipo de dado que armazena coleções de caracteres(ARMAZENA TEXTO)

a = "ChAvEs"
b = "KiKo"

# concatenar = a + b, SE vc fizer assim ela vai unir as variaveis + vai ficar zoado pq n tem espaçemento entre elas
concatenar = a + " " + b
print(concatenar)

# Para descobrir o tamanho de uma strig vc usa a função "len"
tamanho = len(concatenar)
print(tamanho)# lembreçe que ele começa a contar no 0

# Navegação pelo indice, estrutura ==  variavel[posição], lembrando q td começa na posição 0
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
# se vc pedir uma posição que não exista ele dará erro, erro de indice fora do tamanho

# Digitar pedaçõs de String, de uma posição ate a outra
print(concatenar[0:5]) # imprima da posição 0 até a posição 5
print(concatenar[0:]) # Imprima TUDO
print(concatenar[3:10]) # IGNORE DA POSIÇÃO 2 PRA BAIXO E MOSTRE DA POSIÇÃO 3 ATÉ A POSIÇÃO 10
print(concatenar[0:-1]) # De 0 até a ultima posição -1
print(concatenar[::-1]) # Imprimindo ao contrario


# Deixar td em Maiusculo
print(concatenar.upper())

# Deixar td em Minusculo
print(concatenar.lower())

# POREM, ESSA FUNCÇÃO NÃO ALTERA O VALOR DA VARIAVEL, SÓ ESTA PRINTANDO, PARA ADD A FUNÇÃO A VRIAVEL É SÓ IGUALALA
concatenar = concatenar.upper() # Assim ela sempre vai ser Maiuscula
concatenar = concatenar.lower() # Assim ela sempre vai ser Minuscula

# Remover epasços ou/e caracteres especiais
concatenar = concatenar + "\n" # "\n" é 1 caracter especial que faz quebra delinha
print(concatenar)
print(concatenar.strip())

# Converter para Lista
x = "era uma vez na terra da pqp de narnia"
x = x.split()# o () vazio ele separa por espaços
print(x)
# agr converter pra lista porem removendo 1 letra
x = "era uma vez na terra da pqp de narnia"
x = x.split("a") # ele vai quebrar por letras, nesse caso a letra "a", POREM é o "a" MINUSCULO, ele não mudaria se fosse o "a" MAIUSCULO
print(x)

# Buscando na string, descobrir que posição aparece determinada palavra
x = "era uma vez na terra da pqp de narnia"
busca = x.find("terra")
print(busca)
# agr quero que mostre da posição da busca até o final
print(x[busca:])
# caso ele não encontre a palavra(substring) ele retornará -1

# Substitur a palavra de uma string
x = "era uma vez na terra da pqp de narnia"
jutsu = x.replace("terra"," CASA DO KRL")
print(jutsu)