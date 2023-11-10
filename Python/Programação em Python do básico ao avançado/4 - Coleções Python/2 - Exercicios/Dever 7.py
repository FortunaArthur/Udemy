#7
l = []
for i in range(1,11):
    a = int(input("Valor: "))
    l.append(a)

print(l)
print("Valor Maior:",max(l), "Posição:",l.index(max(l)))