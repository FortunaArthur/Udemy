#9
l = []
p = []
for i in range(1,7):
    a = int(input("Valor: "))
    l.append(a)

for i in l:
    if i % 2 == 0:
        p.append(i)

print("Ordem Inversa")
print(p[::-1])