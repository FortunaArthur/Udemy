import random
# Buscar 1 numero aleatorio de 0 a 100
numero = random.randint(0,100)
print(numero)

# metodo choice
lista = [1,2,3,4,56,7,8,43,0]
numero = random.choice(lista)# ele vai escolher 1 numero aleatorio da lista
print(numero)

# Travar em 1 só numero
random.seed(1)# ele é só pra dar o msm resultado
numero = random.randint(0,100)
print(numero)