# São listas de associações compsotas por chave e valor
# ele é declardo por chaves{} POREM vc usa colchetes[] para buscar valor

                #chave : valor,    chave : valor,    chave : valor,
meu_dicionario = {"A":"ACEM",      "P":"PICANHA",    "F":"FRALDINHA"}
# SE VC FIZER
# print(meu_dicionario[0]) vai dar erro PQ dicionario não tem 1 ordem correta, não é por localização
# vc chama pelas chaves
print(meu_dicionario["P"]) #Lembrando que tem q ser akele caracter da chave, num inveta de botar a chave minuscula e pedir pra pesquisar em maisucula q da erro isso ai
print(meu_dicionario) # ASSIM VC MOSTRA TD, chave e valor

# Percorrendo o dicionario

for chave in meu_dicionario: # a variavel temporaria "chave" vai percorrer as chaves do dicioanrio,+ da pra pegar os valores diretamente tb 
    print(chave)# AKI ELE MOSTRA AS CHAVES
    print(meu_dicionario[chave]) # AKI ELE MOSTRA OS VALORES CORRESPONDENTES A CHAVE DO MOMENTO

# IMPRIMIR BUNITIN
for i in meu_dicionario:
    print ( i + ":" + meu_dicionario[i])# TÁ BUNITIN

#Função itens() keys() vales()
print(meu_dicionario.items())# Vai converter o dicionario me uma tupla

print(meu_dicionario.keys())# retorna as chaves

print(meu_dicionario.values())# retorna os valores

# MOSTRAR BUNITIN
for x in meu_dicionario.items():
    print(x)

for y in meu_dicionario.keys():
    print(y)

for z in meu_dicionario.values():
    print(z)

