#57
n1 = int(input('número 1: '))
n2 = int(input('número 2: '))

soma = []

for num in range(n1, n2+1):
    primo = True

    for i in range(2, num):
        if num % i == 0:
           primo = False

    if primo:
        soma.append(num)

print(len(soma))