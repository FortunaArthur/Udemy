#18
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite outro numero: "))

print("MENU" + "\n"
"1 : Somar" + "\n"
"2 : Subtrair" + "\n"
"3 : Dividir" + "\n"
"4 : Multiplicar" + "\n")

escolha = int(input("Qual opção vc escolhe: "))

if escolha == 1:
    print(f"{n1} + {n2} = {n1+n2}")

elif escolha == 2:
    print(f"{n1} - {n2} = {n1-n2}")

elif escolha == 3:
    print(f"{n1} / {n2} = {n1/n2}")

elif escolha == 4:
    print(f"{n1} * {n2} = {n1*n2}")

else:
    print("Valor errado")