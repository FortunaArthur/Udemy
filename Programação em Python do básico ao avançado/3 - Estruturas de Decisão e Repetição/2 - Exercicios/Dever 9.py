#9
n = 1 #vezes
l = []

while n <= 10:
  a = int(input("Numero: "))
  n = n + 1
  if a % 2 != 0:
    l.append(a)

print(f"Lista de Impares:  {l}")

#OU

n = int(input("Numero: "))
for i in range(1, n+1):
  if i % 2 != 0:
    print(i, end=". ")