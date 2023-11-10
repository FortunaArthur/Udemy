#36
l = []
for i in range(1,12):
    a = int(input("N: "))
    l.append(a)

l = sorted(l)
print("Ordem Crescente", l)
print("Ordem Inversa", l[::-1])