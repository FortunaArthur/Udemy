#18
v = int(input("Vezes: "))
l = []

for i in range(0, v):
  n = int(input("Numeros: "))
  l.append(n)
  m = max(l)
  c = l.count(m)

print(f"O numero max foi {m} e ele se repetiu {c} vezes")