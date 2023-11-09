#22
n1 = int(input("Qual sua idede: "))
n2 = int(input("Quantos anos vc prestou serviço: "))

if n1 >= 65:
    print("Pode Aposentar")

elif n2 >= 30:
    print("Pode Aposentar")

elif (n1 >= 65) and (n2 >= 30):
    print("Pode Aposentar")

else:
    print("Não pode Aposentar")