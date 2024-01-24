#24
n = (int(input('Numeros: ')))
l = []
for i in range (1, n):
    if n % i == 0:
        l.append(i)
print(sum(l))