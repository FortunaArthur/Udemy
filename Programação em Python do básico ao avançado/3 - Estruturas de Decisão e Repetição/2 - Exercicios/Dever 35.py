#35
l = []
n1 = int(input("Começo: "))
n2 = int(input("Fim: "))

if n1 > n2:
    print("Intervalo de Valores Invalidos")

else:
    for i in range(n1,n2+1):
        if i % 2 != 0:
            l.append(i)

print(sum(l))