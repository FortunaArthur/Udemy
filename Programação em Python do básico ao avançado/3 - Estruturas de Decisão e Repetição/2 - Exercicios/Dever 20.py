#20
c1 = 0
l1 = []
c2 = 0
l2 = []
while True:
  n = (int(input('Numeros: ')))

  if n == 1000:
    break

  elif n % 2 == 0:
    l1.append(n)
    c1 += 1

  elif n % 2 != 0:
    l2.append(n)
    c2 += 1

print(f"Lista de numeros pares {l1} Quantos numeroes pares tem no total {c1}")
print(f"Lista de numeros impares {l2} Quantos numeroes impares tem no total {c2}")