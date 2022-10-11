minha_lista1 = ["churrasco", "camarão", "dinehiro"]
minha_lista2 = [1,2,3,4,5,6,7,8,9,10]
minha_lista3 = ["Fruta", 99.99, 10, False]

# Printar Valores das listas
print(minha_lista1,"\n",minha_lista2, "\n", minha_lista3)

# Printar Indices(Posições) da lista
print(minha_lista1[1])# Vai printar o camarão, PQ COMEÇA TD NO INDICE 0
# print(minha_lista1[3]), #Vai dar erro de fora do tamanho "IndexError: list index out of range"
print(minha_lista2[5])
print(minha_lista3[3])

# Navegar Pelos Elementos da Lista
for item in minha_lista1: #Vai mostrar item por item percorrido durante alista com o laço FOR
     print(item)

# Descobrir o tamnho de uma lista
tamanho = len(minha_lista2) # o len() vai retornar a quantidade de elesmentos da lista
print(tamanho)

# Adicionar Elementos a lista
minha_lista3.append("PICANHA") # Vai adicionar na ultima posição
print(minha_lista3)

# Verificar se o Elemento Pertence a Lista
if "JOOJ" in minha_lista1:
    print("Chaves passou por aki")

elif 8 in minha_lista2:
    print("OIIITÃAAOOO")

else:
    print("XIUU")

# Remover Elemetos da lista
del minha_lista2 [4:9] # Ele vai remover da posição 4 até a posição 9
print(minha_lista2)
# Apagar a lista td
del minha_lista3 [:]
print (minha_lista3) # Vai mostrar 1 lista vazia

# Criar uma lsiat vazia
minha_lista4 = []
# nela vc pode adicionar itens dps, tipo
minha_lista4.append("Fraldinha")
minha_lista4.append("Costela")
minha_lista4.append("Picanha")
print(minha_lista4)

# Ordenar a lista
listinha = [1,2,5,6,87,9,43234,56,7,887,9809,324,2341,5678,1234,65477,8234,234,0]
listinha.sort() # Metdodo sort() vai alterar a lista original, ele não retorna nada
print(listinha)
lista = sorted(listinha) # Metodo sorted() tem que ser aplicavel a alguma variavel, ai ele vai força a ordenação e te retornar a lista ordenada
print(lista)

# Ordem Inversa (Decrescente)
listinha.sort(reverse=True)
print(listinha)
listinha.reverse() # Metodo reverse() vai pegar o ultimo elemento e jogar pra 1° posição e por ai vai
print(listinha) # Ele vai REVERTER e Não Ordenar do menor pro maior

# Ordem Alfabetica
listona = ["PICANHA", "CUSTELINHA", "FRANGO", "ACEM", "FRALDINHA", "MAMINHA", "LINGUIÇA"]
listona.sort()
print(listona)
listona.sort(reverse=True)
print(listona)
