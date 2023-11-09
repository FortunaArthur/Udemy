#30
n = (int(input('Numeros: ')))
l1 = []
l2 = []
l3 = []
l4 = []

for i in range (1 , n+1, ):
    l1.append(i)
print(f"Operação 1: {sum(l1)}")

#NUM FAÇO MENOR KARALHA DE IDEIA DE COMO FAZER O 2
# FICO ASSIM
for i in range (1 , n+1):

    if i % 2 == 0:
        f = i - (2*i)
        l2.append(f)

    else:
        l3.append(i)

print(l2, l3)
f = sum(l3) + sum(l2)
print(f)

for i in range (1 , n+1, 2):
    l4.append(i)
print(f"Operação 3: {sum(l4)}")