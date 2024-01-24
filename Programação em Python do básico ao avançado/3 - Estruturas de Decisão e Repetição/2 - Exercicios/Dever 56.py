#56
n = 2000000

soma = []

for num in range(2, n):
    primo = True

    for i in range(2, num):
        if num % i == 0:
           primo = False

    if primo:
        print(num)
        soma.append(num)

print(sum(soma))