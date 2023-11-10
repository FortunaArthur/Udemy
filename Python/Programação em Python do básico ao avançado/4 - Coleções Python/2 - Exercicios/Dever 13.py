#13
l = []

for i in range(1,6):
    a = float(input("N: "))
    l.append(a)

print("Posição do Maior:",l.index(max(l)))
print("Posição do Menor:",l.index(min(l)))