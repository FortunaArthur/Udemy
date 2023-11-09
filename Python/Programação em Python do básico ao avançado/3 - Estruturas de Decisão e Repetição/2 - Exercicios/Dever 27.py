#27
n = (int(input('Numeros: ')))
l = []
for i in range(1, n+1):
    b = 1/i
    l.append(b)

h = 1 + sum(l)
print(f"H(n) = {h}")