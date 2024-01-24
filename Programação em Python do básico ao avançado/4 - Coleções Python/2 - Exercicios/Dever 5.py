#5
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = []
for i in l:
    if i % 2 == 0:
        p.append(i)

print("Possui", len(p), "valores pares")
print("Lista dos Valores")
print( *p, sep=', ')