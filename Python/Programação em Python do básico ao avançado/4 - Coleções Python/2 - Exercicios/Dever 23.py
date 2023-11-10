#23
A = []
B = []

for i in range(1,6):
    a = float(input("Valor A: "))
    b = float(input("Valor B: "))
    A.append(a)
    B.append(b)

produto_escalar = []

for x in A:
    for y in B:
        p = x * y
    produto_escalar.append(p)

print("Produto Escalar =",sum(produto_escalar))