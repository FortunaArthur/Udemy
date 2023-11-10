#16
l1 = []
l2 = []

for i in range(1,6):
    a = int(input("Valor: "))
    l1.append(a)
    l2.append(float(a))

print("\n0 - cabo\n"
"1 - Print\n"
"2 - Ordem invertida\n")

while True:
    escolha = int(input("Escolha: "))

    if escolha == 0:
        exit
        False
        break

    elif escolha == 1:
        print(l1,"\n")
        print(l2)
        False
        break

    elif escolha == 2:
        print(l1[::-1],"\n")
        print(l2[::-1])
        False
        break

    else:
        print("Codigo Invalido")