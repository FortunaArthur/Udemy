#21
n1 = float(input("Digite 1 numero: "))
n2 = float(input("Digite outro numero: "))

print("MENU" + "\n"
"1 : Somar" + "\n"
"2 : Subtrair Maior pelo Menor" + "\n"
"3 : Produto entre os 2 (Multiplicação)" + "\n"
"4 : Divisão entre os 2 (Não pode ser numero 0)" + "\n")

escolha = int(input("Qual opção vc escolhe: "))

if escolha == 1:
    print(f"{n1} + {n2} = {n1+n2}")

elif escolha == 2:
   if n1 > n2:
    print(f"{n1} - {n2} = {n1-n2}")
   else:
    print(f"{n2} - {n1} = {n2-n1}")

elif escolha == 3:
    print(f"{n1} * {n2} = {n1*n2}")

elif escolha == 4:
    if n1 and n2 > 0:
        print(f"{n1} / {n2} = {n1/n2}")
        print(f"{n2} / {n1} = {n2/n1}")
    else:
        print("Valor 0 não divide")

else:
    print("Valor errado")