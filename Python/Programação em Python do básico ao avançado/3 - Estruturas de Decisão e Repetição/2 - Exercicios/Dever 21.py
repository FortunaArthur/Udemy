#21
c1 = 0
l1 = []
c2 = 0
l2 = []
count = 0
mult =  1
while True:
    n = (int(input('Numeros: ')))
    if n == 1000:
        break
    if n % 2 == 0:
        l1.append(n)
        c1 +=1
        count += n
    else:
        l2.append(n)
        c2 += 1
        mult *= n

print(f"Lista de numeros pares {l1}\nQuantos numeroes pares tem no total {c1}\nQual a soma dos numeros pares {count}")
print(f"Lista de numeros impares {l2}\nQuantos numeroes impares tem no total {c2}\nQual a multiplicacao dos numeros impares {mult}")