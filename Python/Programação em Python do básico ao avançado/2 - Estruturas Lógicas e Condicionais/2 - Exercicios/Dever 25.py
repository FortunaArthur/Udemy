#25
D = (b**2) - (4 * (a * c))

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

if a != 0:
    print("Não é equação de 2° grau")

else:
    if D < 0:
        print("Não existe raiz")

    elif D == 0:
        print(f"{(-b + (D ** 0.5)) / (2 * a)}")
        print("Raiz Unica")

    elif D >= 0:
        print(f"1° raiz : {(-b + (D ** 0.5)) / (2 * a)}")
        print(f"2° raiz : {(-b - (D ** 0.5)) / (2 * a)}")