# imprimir valores concatenando uma lista com a outra
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = ["PICANHA", "CUSTELINHA", "FRANGO", "ACEM", "FRALDINHA", "MAMINHA", "LINGUIÇA"]
# ele vai compactar as 2 listas como 1 só pr apercorrer com laço for
for numero, nome in zip (lista1, lista2):
    print(numero, nome)
# ele vai pegar o 1° item da lista 1 e jogar pra nuemro, e o 1° item da lista 2 e jogar pra nome, e por ai vai
# vamo tentar com 3 listas
print("\n")
lista3 = ["Ketshup", "Mostarda", "Azeite", "Não tem Preço", "jojo", "jaja", "jeje"]
for numero, nome, condimentos in zip (lista1, lista2, lista3): # Concatenando 3 listas
    print(numero, nome, condimentos)
    # pode fazer isso pra quantas listas quiser