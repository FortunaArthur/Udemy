#27
# https://acervolima.com/programa-python-para-verificar-se-um-numero-e-primo-ou-nao/
l = []

for i in range(1,11):
    a = int(input("Valor: "))
    l.append(a)

primos = []
N_primos = []

for num in l:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                #print(num, "is not a prime number")
                N_primos.append(num)
                break
        else:
            #print(num, "is a prime number")
            primos.append(num)

    else:
        #print(num, "is not a prime number")
        N_primos.append(num)

inds = []
for i in primos:
    inds.append(l.index(i))

print("Numeros primos:", primos)
print("Posição dos numeros primos na lista", inds)