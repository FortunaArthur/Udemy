#15
l = []

for i in range(1,21):
    a = int(input("N: "))
    l.append(a)

print(l)
print("Eliminando elementos repetidos")
print(sorted(set(l)))