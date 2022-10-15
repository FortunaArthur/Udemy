listona = ["PICANHA", "CUSTELINHA", "FRANGO", "ACEM", "FRALDINHA", "MAMINHA", "LINGUIÇA"]
# quer se obter o indice seguido dos nomes da lista, como range() e len() isso se resolve

# o range vai criar um vetor e o len vai medir o tamanho
# for i in range(len(listona)):
# e pra imprimir da forma q ele quer é só colocar i, lista em sua posição: lista[i]
#    print(i, listona[i])

# POREM, TEM OUTRA FORMA MELHOR
# vc vai inidicar 2 valores ( os nomes vc escolhe)
for indice, nome in enumerate(listona):
    # coloquei de forma facil os valores q ele vai retornar, pq é bem isso msm
    print(indice, nome)