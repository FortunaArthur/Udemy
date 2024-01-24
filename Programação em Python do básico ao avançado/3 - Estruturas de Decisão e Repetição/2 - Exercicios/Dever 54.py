#54
# https://acervolima.com/programa-python-para-verificar-se-um-numero-e-primo-ou-nao/
num = int(input("Numero: "))

if num > 1:

    for i in range(2, num):

        if (num % i) == 0:
            print(num, "Primo")
            break
    else:
        print(num, "primo")

else:
    print(num, "Não Primo")