#46
n = input("Escreve 1 numero INTEIRO ai: ")
#Transformo o número digitado em uma lista
n = list(n)
#Faço a orndenação inversa da lista, aqui eu já teria um resultado bem próximo
n.reverse()
print(n, type(n))
#Converto a lista para uma string e depois para inteiro
n = int("".join(n))
print(n)