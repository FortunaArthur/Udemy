# Vai pegar uma função e aplciar a todos elementos de uma lista
def dobro (x):
    return x*2

valor = [1,2,3,4,5]
print(dobro(valor)) # fazendo isso vc está concatenando e tendo 2 copias da lista
# map recebe 2 argumentos
print(map(dobro, valor))# assim ele vai imprirmir o obejto map

# + da pra ver ela em laço
dobrado  = map(dobro, valor)
for i in dobrado:
    print(i)
# OU
dobrado = list(map(dobro, valor))
print(dobrado)