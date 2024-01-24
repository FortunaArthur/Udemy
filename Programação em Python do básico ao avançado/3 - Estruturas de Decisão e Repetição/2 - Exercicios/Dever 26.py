#26
l1 = []
#n = (int(input('Numeros: ')))
#OU
#n = 0
while True:
  n += 1
  if (n % 11 == 0) or (n % 13 == 0) or (n % 17 == 0):
    l1.append(n)
    break

print(l1)