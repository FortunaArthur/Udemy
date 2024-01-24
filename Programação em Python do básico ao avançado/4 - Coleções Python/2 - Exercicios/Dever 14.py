#14
from collections import Counter
l = []

for i in range(1,11):
    a = float(input("N: "))
    l.append(a)

c = Counter(l)

print("Numero : VZ de Repetição")
print(c)