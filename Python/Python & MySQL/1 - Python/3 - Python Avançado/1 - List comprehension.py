# Compreensão de Lista

x = [1,2,3,4,5]
# quero fazer uma l nova lista com os quadrados da 1° lista
# uma forama simples de fazer isso seria o for
'''''''''''''''
y = []
for i in x:
    a = i**2
    y.append(a)
print(y)
'''''''''''''''
# Tem uma forma melhor
# y = [valor que vai adiconar / laço / condição]
    #valor / laço
y = [i**2 for i in x] # é a msm coisa do for só 1 em uma linha
print(y)

# apenas numeros impares de x
# Valor / Laço / Condição
z = [i for i in x if i % 2 != 0]
print(z)