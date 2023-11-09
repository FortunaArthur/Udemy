#28
import math
n = (int(input('Numeros: ')))
l = []
l2 = []
for i in range(1, n+1):

    l.append(i)
    #Tem que importar a porra do MATCH se n se n multiplica os valores da lista
    N = math.prod(l[::-1])

    s = 1/N
    l2.append(s)

E = 1 + sum(l2)
print(f"E = {E}")