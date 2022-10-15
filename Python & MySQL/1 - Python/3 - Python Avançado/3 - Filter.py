# Flitrar uma determinada condição pra adicionar em outra lista
lista = [1,2,3,4,56,7,8,43,0,99,81,44,66,77,22]
# condição aki vamo usar funções
def par(i):
    if i % 2 == 0:
        return i

def impar(i):
    if i % 2 != 0:
        return i
# aplicar a função par() e usar a lista como argumento, recebe 2 argumentos
pares = filter(par, lista)
# ele vai pegar os valores da lista e valiar com base a condição par() e retornar só os valores pares
print(pares)# se vc fizer isso ele só vai retornar o objeto do tipo filter, então vamos convertelo
print(list(pares))

# Msm coisa pros impares
impares = filter(impar, lista)
print(list(impares))

# resumo: vc filtra os elementos de uma lista com base outra função para isso