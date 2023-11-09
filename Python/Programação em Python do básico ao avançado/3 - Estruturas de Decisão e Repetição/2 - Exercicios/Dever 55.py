#55
# https://pt.stackoverflow.com/questions/454612/a-soma-dos-n-primeiros-n%C3%BAmeros-primos
n = int(input('Digite um número inteiro positico: '))
soma = 0

for num in range(2, n + 1):
    primo = True

    for i in range(2, num):
        if num % i == 0:
           primo = False

    if primo:
        print(num)
        soma += num

print(soma)