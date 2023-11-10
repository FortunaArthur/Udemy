#22
A = []
B = []

for i in range(1,11):
    a = int(input("Valor A: "))
    b = int(input("Valor B: "))
    A.append(a)
    B.append(b)

pares = []
impares = []

for x in A:
    if x % 2 == 0:
        pares.append(x)

    elif x % 2 != 0:
        impares.append(x)

for y in B:
    if y % 2 == 0:
        pares.append(y)

    elif y % 2 != 0:
        impares.append(y)

print("Lista de Pares", pares)
print("Lista de Impares",impares)