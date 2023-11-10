#3
def nPorN(n):
    if n == 0:
        print("É ZERO")
    elif n % 2 == 0:
        print("Positivo")
    else:
        print("Negativo")

nPorN(int(input("Numero: ")))