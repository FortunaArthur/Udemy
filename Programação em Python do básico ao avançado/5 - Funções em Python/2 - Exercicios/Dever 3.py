#3
def nPorN(x):
    try:
        n = int(x)
        if n == 0:
            print("É ZERO")
        elif n > 0:
            print("Positivo")
        else:
            print("Negativo")
    except ValueError:
        print("Tem que ser um número inteiro")

nPorN(input("Número: "))
