#11
l = []
p = []
I = []

for i in range(1,11):
    a = float(input("N: "))
    l.append(a)

for i in l:
    if i > 0:
        p.append(i)
    elif i < 0:
        I.append(i)

print("Quantidade de Negativos ==",len(I))
print("Soma dos Positivos ==", sum(p))