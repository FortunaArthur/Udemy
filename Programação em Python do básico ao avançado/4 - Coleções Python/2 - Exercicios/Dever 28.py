#28
l = []

for i in range(1,11):
    a = int(input("Valor: "))
    l.append(a)

v1 = []
v2 = []

for x in l:
    if x % 2 == 0:
        v2.append(x)

    elif x % 2 != 0:
        v1.append(x)

print("Lista de Pares", v2)
print("Lista de Impares", v1)