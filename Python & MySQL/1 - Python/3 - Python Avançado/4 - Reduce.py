# recebe uma lista e retorna 1 unico valor para essa lista
from functools import reduce
from os import lstat

lista = [1,2,3,4,56,7,8,43,0,99,81,44,66,77,22]

# vamos fazer ocm soma de valores
def soma (x,y):
    return x + y

somar = reduce(soma, lista)
# ele vai receber na função x sendo o valor e y a soma de tds os valores
print(somar)